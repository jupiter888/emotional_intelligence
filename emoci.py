from valid import *
#module 1

def begin():
    print("Going through an emotional experience can be challenging.\n")


def feel():
    print("How do you Feel?\n-----------------\n")
    emo_dict = {0: "Angry", 1: "Afraid", 2: "Disgusted", 3: "Sad", 4: "Joyful"}
    for emo in emo_dict:
        print(emo, ":", emo_dict[emo])
    feeling = inputNumber("\n-----------------\nEnter # for how you feel")
    return feeling #int to use as key value for outer function


#nest the functions in the end!!!!!!!! understand( feel() )
def understand(feelings):

    this_feeling_explained_dict = {0: "Anger consists of being annoyed and fury",
                                   1: "Fear includes anxiety and terror",
                                   2: "Disgust contains dislike and loathing",
                                   3: "Sadness contains disappointment and despair",
                                   4: "Enjoyment contains harmony and bliss"}
    print("=======================================\nUnderstanding this feeling:\n" + this_feeling_explained_dict[feelings]+"\n=======================================")


def cause():
    print(
        "\nOur emotions unfold in a consecutive order,\nusually beginning with a trigger.\nThe trigger initiates an emotional experience, and we respond...\n")


def trigger():
    print("====================================\nContext of trigger:\n")
    contexts = {0: "Circumstance in life and your feelings",
                1: "An event occurring/occurred",
                2: "Our overall perception of the world",
                3: "Interaction with Spouse or family",
                4: "Interaction with stranger"}
    for option in contexts:
        print(option, ":", contexts[option])
    triggered = inputNumber("====================================\nEnter context # to analyze the experience\n")
    return triggered


# in the end nest these two: response(trigger())
def response(triggered):
    print("====================================\nResponses common to the trigger:\n")
    responses = {
        0: "Some people suppress feelings of frustration in the work environment, but scream insanely to express frustrations with a family member/spouse/friend.",
        1: "Some people might avoid feeling anxiety at work, but may contemplate utter horror once home",
        2: "We might avoid feeling strong dislike towards others at work, however we may find ourselves feeling aversion to individuals in mass media. ",
        3: "It is possible to withraw from feeling helpless in public, but seek comfort at home.",
        4: "We often express our amusement to our friends, however we might actually experience our bliss quietly while alone"}
    print(responses[triggered])


def strategy():
    print(
        "An important aspect about being emotionally conscious, is allowing yourself to feel\nThere is no need to rationalize your emotions,so stop trying to\nEmotional intelligence can be harvested with healthy strategies")
    strategies_list = ["Sipping oxygen, take a DEEP BREATH...surrender.",
                       "Drink something refreshing, ideally clean water and not alcohol.\nAlcohol does not solve problems, it only postpones them.",
                       "Eat something delicious. Comfort food can help a lot.\nTry to aim towards a healthy option.",
                       "Get some rest, sleep can be medicinal.",
                       "Channeling your emotions into art is one special way of feeling more at ease,\nbecause you can express yourself in an abstract thorough manner."]
    strategies_numbers_list = [1, 2, 3, 4, 5]
    emotional_intelligence_dict = dict(zip(strategies_numbers_list, strategies_list))
    for strategy in emotional_intelligence_dict:
        print(strategy, ":", emotional_intelligence_dict[strategy]+"\n\n\n")


def continue_onward(str):
    print("--Press any key + Enter to "+str)