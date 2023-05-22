import numpy as np
from flask import Markup

import psynet.experiment
from psynet.asset import DebugStorage, FastFunctionAsset, S3Storage  # noqa
from psynet.consent import NoConsent
from psynet.prescreen import AntiphaseHeadphoneTest
from psynet.modular_page import PushButtonControl, ModularPage
from psynet.js_synth import JSSynth, Note, HarmonicTimbre
from psynet.timeline import Timeline, Event

from psynet.page import InfoPage, SuccessfulEndPage, VolumeCalibration
from psynet.timeline import Timeline
from psynet.trial.static import StaticNode, StaticTrial, StaticTrialMaker

from .melodies import convert_interval_sequence_to_absolute_pitches, sample_reference_pitch


from .consent import consent  # TODO: use my Oxford consent here whean ready
from .instructions import instructions
from .questionnaire import debrief, questionnaire, STOMPR, TIPI
from .volume_calibration import volume_calibration


##########################################################################################
# Global
##########################################################################################
# Set the size and range of the grid for the stimulus space
NUM_PARTICIPANTS = 100

N_REPEAT_TRIALS = 6
INITIAL_RECRUIT_SIZE = 20

roving_width = 2.5
roving_mean = dict(
    default=55,
    low=49,
    high=61
    )
roving_mean = roving_mean["default"]

num_notes = 3

# timbre
note_duration_tonejs = 0.8
note_silence_tonejs = 0
TIMBRE = dict(
    default=HarmonicTimbre(
        attack=0.01,  # Attack phase duration in seconds
        decay=0.05,  # Decay phase duration in seconds
        sustain_amp=0.6,  # Amplitude fraction to decay to relative to max amplitude --> 0.4, 0.7
        release=0.55,  # Release phase duration in seconds
        num_harmonics=10,  # Acd ctual number of partial harmonics to use
        roll_off=14,  # Roll-off in units of dB/octave,
    )
)

##########################################################################################
# Stimuli
##########################################################################################
# Here we define the stimulus set in an analogous way to the static_audio demo,
# except we randomise the start_frequency from a continuous range.

# TODO: Kevin, we just want to use integer semitones, and make sure the trials per particiapnt is right
# TODO: 120 trials maximum

grid_size = 15
grid_range = 7

TRIALS_PER_PARTICIPANT = grid_size * grid_size  # TODO: this calculation is wrong


nodes = [
    StaticNode(
        definition={
            # "intervals": interval,
            "x_int": x,
            "y_int": y,
        },
    )
    for x in np.linspace(-grid_range, grid_range, grid_size)
    for y in np.linspace(-grid_range, grid_range, grid_size)
    # for interval in intervals
]


class RatingTrial(StaticTrial):
    time_estimate = 5
    # wait_for_feedback = True

    def finalize_definition(self, definition, experiment, participant):
        reference_pitch = sample_reference_pitch(
            roving_mean,
            roving_width,
        )
        definition["reference_pitch"] = reference_pitch

        intervals = [definition["x_int"], definition["y_int"]]
        definition["intervals"] = intervals

        definition["pitches"] = convert_interval_sequence_to_absolute_pitches(
                intervals=intervals,
                reference_pitch=reference_pitch,
                reference_mode="previous_note",   # pitch mode
            )
        return definition

    def show_trial(self, experiment, participant):

        melody = self.definition['pitches']

        current_trial = self.position + 1
        show_current_trial = f'<i>Trial number {current_trial} out of {(TRIALS_PER_PARTICIPANT + N_REPEAT_TRIALS)} trials.</i>'

        return ModularPage(
            "chord_player",
            JSSynth(
                Markup(f"""
                Please rate the sound for <strong>pleasantness</strong> on a scale from 1 to 7.<br><br>
                {show_current_trial}"""),
                sequence=[Note(x) for x in melody],
                timbre=TIMBRE,
                default_duration=note_duration_tonejs,
                default_silence=note_silence_tonejs
            ),
            PushButtonControl(
                choices=[1, 2, 3, 4, 5, 6, 7],
                labels=[
                    "(1) Very unpleasant",
                    "(2)",
                    "(3)",
                    "(4)",
                    "(5)",
                    "(6)",
                    "(7) Very pleasant",
                ],
                arrange_vertically=True,
            ),
            events={
                "responseEnable": Event(is_triggered_by="promptEnd"),
                "submitEnable": Event(is_triggered_by="promptEnd")
            }
        )


class RatingTrialMaker(StaticTrialMaker):
    performance_check_type = "consistency"
    consistency_check_type = "spearman_correlation"
    give_end_feedback_passed = False

    def compute_bonus(self, score, passed):
        max_bonus = 0.50

        if score is None or score <= 0.0:
            bonus = 0.0
        else:
            bonus = max_bonus * score

        bonus = min(bonus, max_bonus)
        return bonus


class Exp(psynet.experiment.Experiment):
    label = "Melody rating experiment"
    initial_recruitment_size = INITIAL_RECRUIT_SIZE

    variables = {
        "currency": "£",
        "wage_per_hour": 10,
        "window_width": 1024,
        "window_height": 1024,
    }

    timeline = Timeline(
        NoConsent(),
        InfoPage(
            "This experiment requires you to wear headphones. Please ensure you have plugged yours in now.",
            time_estimate=3,
        ),
        # volume_calibration(TIMBRE, note_duration_tonejs, note_silence_tonejs),
        # InfoPage(
        #     """
        #     We will now perform a short listening test to verify that your audio is working properly.
        #     This test will be difficult to pass unless you listen carefully over your headphones.
        #     Press 'Next' when you are ready to start.
        #     """,
        #     time_estimate=5,
        # ),
        # AntiphaseHeadphoneTest(),
        instructions(),
        RatingTrialMaker(
            id_="rating_main_experiment",
            trial_class=RatingTrial,
            nodes=nodes,
            expected_trials_per_participant=TRIALS_PER_PARTICIPANT,
            max_trials_per_participant=TRIALS_PER_PARTICIPANT,
            recruit_mode="n_participants",
            allow_repeated_nodes=False,
            n_repeat_trials=N_REPEAT_TRIALS,
            balance_across_nodes=True,
            target_n_participants=NUM_PARTICIPANTS,
            check_performance_at_end=True,
        ),
        questionnaire(),
        InfoPage("Next, we would like to ask you some questions about your music preferences (0.15 extra bonus)", time_estimate=3),
        STOMPR(),
        InfoPage("Finally, we would like to ask you some questions about your personality (0.15 extra bonus)", time_estimate=3),
        TIPI(),
        # debrief(),
        SuccessfulEndPage(),
    )

    # uncomment for testing
    # test_n_bots = 2
    #
    # def test_experiment(self):
    #     # To run this test, manually change TRIALS_PER_PARTICIPANT to 8 and grid size to 4
    #     super().test_experiment()
    #
    #     nodes = StaticNode.query.filter_by(trial_maker_id="rating_main_experiment").all()
    #
    #     for n in nodes:
    #         n_trials = len(n.infos())
    #         assert n_trials == 1
