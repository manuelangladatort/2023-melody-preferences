from dominate import tags

from psynet.demography.general import Age, Gender
from psynet.demography.gmsi import GMSI
from psynet.demography.pei import PEI
from psynet.modular_page import ModularPage, TextControl, SurveyJSControl
from psynet.page import InfoPage
from psynet.timeline import join


def introduction():
    html = tags.div()
    with html:
        tags.p(
            "Congratulations, you completed the listening part of this experiment!"
        )
        tags.p(
            "Before we finish, we just have a few more questions to ask you. ",
            "They should only take a couple of minutes to complete.",
        )
    return InfoPage(html, time_estimate=10)


def questionnaire():
    return join(
        introduction(),
        Age(),
        Gender(),
        PEI(),
        GMSI(subscales=["Musical Training"]),
        feedback(),
    )


rating_values = [
    {"value": "1", "text": "1"},
    {"value": "2", "text": "2"},
    {"value": "3", "text": "3"},
    {"value": "4", "text": "4"},
    {"value": "5", "text": "5"},
    {"value": "6", "text": "6"},
    {"value": "7", "text": "7"}
]


def STOMPR():
    return ModularPage(
            "stompr",
            "Please indicate your basic preference for each of the following genres using the scale provided.",
            SurveyJSControl(
                {
                    "logoPosition": "right",
                    "pages": [
                        {
                            "name": "page1",
                            "elements": [
                                {
                                    "type": "rating",
                                    "name": "Alternative",
                                    "isRequired": True,
                                    "title": "Please indicate your preference for Alternative music:",
                                    "rateValues": rating_values,
                                    "minRateDescription": "Dislike Strongly",
                                    "maxRateDescription": "Like Strongly",
                                },
                                {
                                    "type": "rating",
                                    "name": "Bluegrass",
                                    "isRequired": True,
                                    "title": "Please indicate your preference for Bluegrass music:",
                                    "rateValues": rating_values,
                                    "minRateDescription": "Dislike Strongly",
                                    "maxRateDescription": "Like Strongly",
                                },
                                {
                                    "type": "rating",
                                    "name": "Blues",
                                    "isRequired": True,
                                    "title": "Please indicate your preference for Blues music:",
                                    "rateValues": rating_values,
                                    "minRateDescription": "Dislike Strongly",
                                    "maxRateDescription": "Like Strongly",
                                },
                                {
                                    "type": "rating",
                                    "name": "Classical",
                                    "isRequired": True,
                                    "title": "Please indicate your preference for Classical music:",
                                    "rateValues": rating_values,
                                    "minRateDescription": "Dislike Strongly",
                                    "maxRateDescription": "Like Strongly",
                                },
                                {
                                    "type": "rating",
                                    "name": "Country",
                                    "isRequired": True,
                                    "title": "Please indicate your preference for Country music:",
                                    "rateValues": rating_values,
                                    "minRateDescription": "Dislike Strongly",
                                    "maxRateDescription": "Like Strongly",
                                },
                                {
                                    "type": "rating",
                                    "name": "Dance",
                                    "isRequired": True,
                                    "title": "Please indicate your preference for Dance/Electronica music:",
                                    "rateValues": rating_values,
                                    "minRateDescription": "Dislike Strongly",
                                    "maxRateDescription": "Like Strongly",
                                },
                                {
                                    "type": "rating",
                                    "name": "Folk",
                                    "isRequired": True,
                                    "title": "Please indicate your preference for Folk music:",
                                    "rateValues": rating_values,
                                    "minRateDescription": "Dislike Strongly",
                                    "maxRateDescription": "Like Strongly",
                                },
                                {
                                    "type": "rating",
                                    "name": "Funk",
                                    "isRequired": True,
                                    "title": "Please indicate your preference for Funk music:",
                                    "rateValues": rating_values,
                                    "minRateDescription": "Dislike Strongly",
                                    "maxRateDescription": "Like Strongly",
                                },
                                {
                                    "type": "rating",
                                    "name": "Gospel",
                                    "isRequired": True,
                                    "title": "Please indicate your preference for Gospel music:",
                                    "rateValues": rating_values,
                                    "minRateDescription": "Dislike Strongly",
                                    "maxRateDescription": "Like Strongly",
                                },
                                {
                                    "type": "rating",
                                    "name": "HeavyMetal",
                                    "isRequired": True,
                                    "title": "Please indicate your preference for Heavy Metal music:",
                                    "rateValues": rating_values,
                                    "minRateDescription": "Dislike Strongly",
                                    "maxRateDescription": "Like Strongly",
                                },
                                {
                                    "type": "rating",
                                    "name": "World",
                                    "isRequired": True,
                                    "title": "Please indicate your preference for World music:",
                                    "rateValues": rating_values,
                                    "minRateDescription": "Dislike Strongly",
                                    "maxRateDescription": "Like Strongly",
                                },
                                {
                                    "type": "rating",
                                    "name": "Jazz",
                                    "isRequired": True,
                                    "title": "Please indicate your preference for Jazz music:",
                                    "rateValues": rating_values,
                                    "minRateDescription": "Dislike Strongly",
                                    "maxRateDescription": "Like Strongly",
                                },
                            ],
                        },
                        {
                            "name": "page2",
                            "elements": [
                                {
                                    "type": "rating",
                                    "name": "New Age",
                                    "isRequired": True,
                                    "title": "Please indicate your preference for New Age music:",
                                    "rateValues": rating_values,
                                    "minRateDescription": "Dislike Strongly",
                                    "maxRateDescription": "Like Strongly",
                                },
                                {
                                    "type": "rating",
                                    "name": "Oldies",
                                    "isRequired": True,
                                    "title": "Please indicate your preference for Oldies music:",
                                    "rateValues": rating_values,
                                    "minRateDescription": "Dislike Strongly",
                                    "maxRateDescription": "Like Strongly",
                                },
                                {
                                    "type": "rating",
                                    "name": "Opera",
                                    "isRequired": True,
                                    "title": "Please indicate your preference for Opera music:",
                                    "rateValues": rating_values,
                                    "minRateDescription": "Dislike Strongly",
                                    "maxRateDescription": "Like Strongly",
                                },
                                {
                                    "type": "rating",
                                    "name": "Pop",
                                    "isRequired": True,
                                    "title": "Please indicate your preference for Pop music:",
                                    "rateValues": rating_values,
                                    "minRateDescription": "Dislike Strongly",
                                    "maxRateDescription": "Like Strongly",
                                },
                                {
                                    "type": "rating",
                                    "name": "Punk",
                                    "isRequired": True,
                                    "title": "Please indicate your preference for Punk music:",
                                    "rateValues": rating_values,
                                    "minRateDescription": "Dislike Strongly",
                                    "maxRateDescription": "Like Strongly",
                                },
                                {
                                    "type": "rating",
                                    "name": "Rap",
                                    "isRequired": True,
                                    "title": "Please indicate your preference for  Rap/hip-hop music:",
                                    "rateValues": rating_values,
                                    "minRateDescription": "Dislike Strongly",
                                    "maxRateDescription": "Like Strongly",
                                },
                                {
                                    "type": "rating",
                                    "name": "Reggae",
                                    "isRequired": True,
                                    "title": "Please indicate your preference for Reggae music:",
                                    "rateValues": rating_values,
                                    "minRateDescription": "Dislike Strongly",
                                    "maxRateDescription": "Like Strongly",
                                },
                                {
                                    "type": "rating",
                                    "name": "Religious",
                                    "isRequired": True,
                                    "title": "Please indicate your preference for Religious music:",
                                    "rateValues": rating_values,
                                    "minRateDescription": "Dislike Strongly",
                                    "maxRateDescription": "Like Strongly",
                                },
                                {
                                    "type": "rating",
                                    "name": "Rock",
                                    "isRequired": True,
                                    "title": "Please indicate your preference for Rock music:",
                                    "rateValues": rating_values,
                                    "minRateDescription": "Dislike Strongly",
                                    "maxRateDescription": "Like Strongly",
                                },
                                {
                                    "type": "rating",
                                    "name": "Soul",
                                    "isRequired": True,
                                    "title": "Please indicate your preference for Soul/R&B music:",
                                    "rateValues": rating_values,
                                    "minRateDescription": "Dislike Strongly",
                                    "maxRateDescription": "Like Strongly",
                                },
                                {
                                    "type": "rating",
                                    "name": "Soundtracks",
                                    "isRequired": True,
                                    "title": "Please indicate your preference for Soundtracks/theme song music:",
                                    "rateValues": rating_values,
                                    "minRateDescription": "Dislike Strongly",
                                    "maxRateDescription": "Like Strongly",
                                },
                                {
                                    "type": "rating",
                                    "name": "Jazz",
                                    "isRequired": True,
                                    "title": "Please indicate your preference for Jazz music:",
                                    "rateValues": rating_values,
                                    "minRateDescription": "Dislike Strongly",
                                    "maxRateDescription": "Like Strongly",
                                },
                            ],
                        },
                    ],
                },
            ),
            time_estimate=5,
            bot_response=lambda: {"rating": "5",},
        )


def feedback():
    return ModularPage(
        "feedback",
        "Do you have any feedback to give us about the experiment?",
        TextControl(one_line=False),
        bot_response="I am just a bot, I don't have any feedback for you.",
        save_answer="feedback",
        time_estimate=20,
    )


def debrief():
    html = tags.div()

    with html:
        tags.p(
            """
            Thank you for participating in this experiment. The purpose of the experiment was to collect data on how we 
            perceive ‘pleasant’ melodies (sequences of musical tones), such as the ones you have been listening to.
            """
        )
        tags.p(
            """
            Pleasantness is very important to understand how we perceive and create musical melodies (the main musical 
            idea in a piece of music, or that part that you can sing or hum along to). Other important aspects melodies 
            are pitch (the series of notes that rise and fall in pitch) and rhythm (the timing and duration of these 
            notes).
            """
        )
        tags.p(
            """
            The data collected during this experiment will help to better understand how people derive pleasure from 
            melodies, studying for the first time all possible melodic combinations and listeners' individual 
            differences at a large scale (testing many melodies and participants from different backgrounds).
            """
        )

    return InfoPage(html, time_estimate=10)
