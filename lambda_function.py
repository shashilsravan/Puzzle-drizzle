from __future__ import print_function
import string
import random

question1 = ["""
            If you add the square of Sai's age to the age of Siri, the sum is 62. But
            if you add the square of Siri's age to the age of Sai, the result is 176. 
            Can you say, what's the age of Sai?
            """,
            7]
            
question2 = [
            """
            When visiting an insane asylum, I asked two inmates to give me their ages.
            They did so, and then, to test their arithmetical powers, I asked them to add
            the two ages together. One gave me 44 as the answer, and the other
            gave 1,280. I immediately saw that the first had subtracted one age from the
            other, while the second person had multiplied them together. What were their sum of the ages?
            """,
            84
            ]

question3 = [
            """
            geetesh has lived one-fourth of his life as a boy, one-fifth as a youth,
            one-third as a man, and has spent thirteen years in his dotage. How old is the gentleman?
            """,
            60
            ]
            
question4 = [
            """
            Devi said. On being asked the ages of his two sons, 
            stated that eighteen more than the sum of their ages is double the age of the elder.
            And six less than the difference of their ages is the age of the younger. What's the eldest member age? 
            """,
            30
            ]
     
question5 = [
            """
            Raju said. 
            "Three years ago I was seven times as old as my sister.
            two years ago I was four times as old. 
            last year I was three times as old. 
            And this year I am two and one-half times as old. " . What's the age of his sister? 
            """,
            4
            ]     
            
question6 = [
            """
            Sharma had nine children, all born at regular intervals. 
            And the sum of the squares of their ages was equal to the square of his own. 
            What was the age of Sharma.
            """,
            48
            ]

question7 = [
            """
            "The steamer," remarked one of our officers home from the East, "was able
            to go twenty miles an hour downstream, but could only do fifteen miles an
            hour upstream.
            So, of course, she took five hours longer in coming up than in going down."
            One could not resist working out mentally the distance from point to point.
            What's the distance must have been in miles?
            """,
            300
            ]
            
question8 = [
            """
            Two cyclists race on a circular track. 
            Siri can ride once round the track in six minutes, and Alexa in four minutes. 
            In how many minutes will siri overtakes alexa?
            """,
            12
            ]

question9 = [
            """
            What is the smallest square number that terminates with the greatest possible number of similar digits? 
            For example, in the case of 144, the square of 12, 
            all the three digits can be decomposed into a smaller digit 1, 2 and 2.
            Of course, 0 is not to be regarded as a digit
            """,
            1444
            ]
            
question10 = [
            "what is the square root of smaller square number containing an even number of digits and a palindrome?",
            836
            ]
            
question11 = [
            """
            what is the longest three digit number, that have all the three digits different.
            And the number should be divisible exactly by, square of sum of the digits of that number.
            """,
            972
            ]
            
question12 = [
            """
            Find the two consecutive cube numbers in integers whose difference shall be a square number? 
            . What is the smallest possible case? Tell the square root of the number. " 
            """,
            13
            ]
            
question13 = [
            """
            Three juvenile highwaymen, returning from the market town movie house,
            called upon an apple woman "to stand and deliver." Tom seized half of the
            apples, but returned ten to the basket; Ben took one-third of what were left,
            but returned two that he did not fancy; Jim took half of the remainder, but
            threw back one that was worm eaten. The woman was then left with only
            twelve in her basket.
            How many apples had she before the raid was made? 
            """,
            40
            ]
            
question14 = [
            """
            A salesman packs his dog biscuits (all of one quality) in boxes containing
            16, 17, 23, 24, and 40 biscuits per box. respectively, and he will not sell them in any
            other way, or break into a box. A customer asked to be supplied with 100 Biscuits.
            of the biscuit. How many boxes he need to deliver exact 100 biscuits.
            Of course, he has an ample supply of boxes of each size.
            """,
            6
            ]
            
question15 = [
                """
                Alfred and Bill together can do a piece of work in twenty-four days. 
                If Alfred can do only two-thirds as much as Bill, 
                how long will it take for alfred to do the work alone? 
                """,
                60
                ]
                
question16 = [
                """
                If one-fifth of a hive of bees flew to the ladamba flower, one-third flew to
                the slandbara, three times the difference of these two numbers flew to an arbor,
                and one bee continued to fly about, attracted on each side by the fragrant
                ketaki and the malati, what was the number of bees?         
                """,
                15
                ]
question17 = [
                """
                The square root of, half the number of bees, in a swarm has flown out upon a jessamine bush.
                Eight-ninths of the whole swarm has remained behind. One female bee flies about a male that is
                , buzzing within the lotus flower into which. He was allured in the night by its sweet odor, 
                but is now imprisoned in it. Tell me the number of bees. 
                """,
                72
                ]
                
question18 = [
                """
                I am a number. If you divide my number by 2, 3, 4, 5, or 6.
                You will find there is always 1 over. But if you divide it by 11 there ain't no remainder. 
                What's more, there is no other number with a lower number. What was my number"
                """,
                121
                ]
                
question19 = [
                """
                I happened to be discussing the tenancy of a friend's property," said the
                Colonel, "when he informed me that there was a 99 years' lease. I asked him
                how much of this had already expired, and expected a direct answer. But his
                reply was that two-thirds of the time past was equal to four-fifths of the time
                to come, so I had to work it out for myself.
                """,
                54]
                
question20 = [
                """
                A body of soldiers was marching in regular column, with five men more in
                depth than in front. When the enemy came in sight the front was increased
                by 845 men, and the whole was thus drawn up in five lines. How many men
                were there in all?
                """,
                4550
                ]

question21 = [
                """
                I am a number. if divided by 2, will give a remainder 1; divided by 3, a remainder 2; 
                divided by 4, a remainder 3; divided by 5, a remainder 4; 
                divided by 6, a remainder 5; divided by 7, a remainder 6; divided by 8, a remainder 7; 
                divided by 9, a remainder 8; divided by 10, a remainder 9. 
                And to make it more simple. I lies between 2000 to 3000. Who am i?
                """,
                2519
                ]
                
question22 = [
                """
                My friend Tompkins loves to spring on you little puzzling questions on
                every occasion, but they are never very profound," said the Colonel. 
                "I was walking round his garden with him the other day when he pointed 
                to a rectangular flower bed, and said: 'If I had made that bed 2 feet broader and
                3 feet longer it would have been 64 square feet larger; but if it had been 3 feet
                broader and 2 feet longer it would then have been 68 square feet larger.
                What is its perimeter?
                """,
                48]
                
question23 = [
                """
                Next door to me, there lived a four brothers of different heights. Their average height is 74.
                And the difference among first three men is two . The difference between the third and fourth man is six.
                What is the height of the tallest brother?
                """,
                80
                ]
                
question24 = [
                """
                Fifty minutes ago if it was four times as many minutes past three o'clock, how many minutes is it. 
                Untill six o'clock?
                """,
                26
                ]
                
question25 = [
                """
                Rohit said. At the time we were married rithika was three forth of my age.
                But now she is only five sixth. what is my age when i am married?
                Hint:  My age is 6 multiple
                """,
                24
                ]
                
question26 = [
                """
                There is a number which is very peculiar.
                This number is three times the sum of its digits. Can you find the number?
                """,
                27
                ]

question27 = [
                """
                I am a number, the second digit of me is smaller than the first digit by 4.
                And if we divide me with the sum of my digits, the quotient would be 7.
                Who am i?
                """,
                84
                ]
                
question28 = [
                """
                The product of three consecutive numbers, when divided by each of them in turn,
                the sum of three quotients will be  74. What was the last number?
                """,
                6
                ]
                
question29 = [
                """
                Siri, ate panner and pani puri for 220 rupees. 
                If panneer costs 200 rupees more than pani puri, then how much does,
                panneer i cost?
                """,
                210
                ]
                
question30 = [
                """
                Some months back this year. I was walking through the park in New York.
                I saw an intelligent looking little boy playing, all by himself on a grass.
                I asked him his age.
                He replied two days back, i was ten years old, and next year i shall be thirteen.
                And also the boy said, if you know what's today you'll be able to figure out my birthday and
                that'll give you my age. How old was the boy?
                """,
                11
                ]

question31 = [
                """
                I am a four digit number.
                If you reverse me, i will be exactly divisble by the original me.
                To make it more simple, i will be between 1000 to 2000.
                """,
                1089
                ]
                
trick1 = ["1",
            """
            Ok. To make it simple, select a number from 1 to 20.
            Add 1 to your selected number.
            Now double your number.
            Add 4 to it.
            And now divide your number by 2.
            And finally remove the number you chose from the result you got after division.
            And Boooom !!!. The number now you have is 3.
            """,
            """
            It can be solved by simple linear equations.
            Let your number be x.
            when you add 1 to it, then it becomes x+1.
            when you double it, it becomes 2x+2.
            After adding 4 to it, it becomes 2x+6.
            Now when u divided by 3, u get x+3.
            After removing your number x from x+3, you get 3 as remainder.
            """]
            
trick2 = [
            "2",
            """
            Ok. Let me guess your age.
            Take the first digit, means tens placed digit in your age.
            And multiply by 5.
            Add 4 to the resultant.
            Now double the resultant.
            Ok now take the second digit of your age and add to the number.
            So if you take 8 from the resultant number, you will get your age.
            Whoa, Interesting right!
            """,
            """
            This problem also can be solved by linear equations.
            Let your age by xy.
            when you take x and multiply by 5, it becomes 5x.
            After adding 4, it becomes 5x+4.
            After doubling, it becomes 10x+8.
            Adding second digit to the resultant makes it as 10x+y+8.
            After removing 8, it becomes 10x+y. Nothing but your age.
            """
            ]
            
trick3 = [
            "3",
            """
            Take a 3 digit number, having, all the three digits same.
            After taking it.
            Divide it with the sum of the three digits.
            Boom!!! You have got 37 now after divison.
            """,
            """
            whatever the number u take,
            it can be 111, 222, 333 and so on to 999.
            If you divide it with sum of their digits. You will get 37
            """]
            
trick4 = [
            "4",
            """
            Take the last digit of your phone number.
            Multiply it by 2.
            Add 5 to the resultant.
            multiply the resultant with 50. Yeah fifty is a larger number. So, You may use calculator now. Hmm. 
            After multiplying by 50. Add 1770 to it. Yeah to add 1770. You can use calculator again.
            Now finally remove your birthday year from the resultant.
            Boom!!!. Let me guess. I think You've got a three digit number.
            With first digit being your last digit of the phone number.
            And the last two digits denotes your age.
            """,
            """
            Let your number be x.
            After multiplying with 2, it becomes 2x.
            Add 5 to resultant makes it 2x+5.
            After multiplying with 50, you will get 100x + 250 .
            Now when u add 1770 to it. It results in 100x + 2020. Which is our current year.
            so if you remove birthday year, you will definitely get your age.
            And with 100x, you will get x being in 100th place digit.
            """
            ]
            
trick5 = ["5",
            """
            Pick a number between 1 to 10. But not 1 and 10.
            Multiply the number with 9.
            If you got a two digit number, then add the two digits of the number.
            Now, subtract 5 from it. And relate a letter associated with that number.
            For example if your result is 1, the letter would be A.
            if result is 2, the letter would be B. and so on.
            Boom!!! The letter you've got is D.
            """,
            """
            When you pick digits from 2 to 9.
            whatever the digit it is, when you multiply by 9, you will get a two digit number.
            Which results in nine, when you add those two numbers.
            For example in 18,27,36 to 81. All the digits sum will be 9 in any case.
            So when you subtract 5 from it.
            You will definitely get 4. Then 4 is equal to D.
            """
            ]
            
tricks = [trick1, trick2, trick3, trick4, trick5]

easy = [question1, question3, question6, question12, question14,
            question15, question23 ,question24, question26, question29, question31]
medium = [question4, question5, question8, question10, question11, 
            question16, question18, question25, question27, question28]
hard = [question2, question7, question9, question13, question17, 
            question19, question20, question21, question22, question30]

def build_speechlet_response(title, output, reprompt_text, should_end_session):
    return {
        'outputSpeech': {
            "type": "SSML",
            "ssml": """<speak>"""+ output + "</speak>"

        },
        'card': {
            'type': 'Simple',
            'title':  title,
            'content':  output
        },
        'reprompt': {
            'outputSpeech': {
                'type': 'PlainText',
                'text': reprompt_text
            }
        },
        'shouldEndSession': should_end_session
    }

def build_speechlet_response_music3(title, output, reprompt_text, should_end_session):
    return {
        'outputSpeech': {
            "type": "SSML",
            "ssml": """<speak> <audio src="soundbank://soundlibrary/home/amzn_sfx_food_frying_01"/>"""+ output + 
            """ <audio src="soundbank://soundlibrary/ui/gameshow/amzn_ui_sfx_gameshow_waiting_loop_30s_01"/> </speak>"""
        },
        'card': {
            'type': 'Simple',
            'title':  title,
            'content':  output
        },
        'reprompt': {
            'outputSpeech': {
                'type': 'PlainText',
                'text': reprompt_text
            }
        },
        'shouldEndSession': should_end_session
    }
    
def build_speechlet_response_music2(title, output, reprompt_text, should_end_session):
    return {
        'outputSpeech': {
            "type": "SSML",
            "ssml": """<speak> <audio src="soundbank://soundlibrary/magic/amzn_sfx_fairy_melodic_chimes_01"/> <voice name="Matthew"><lang xml:lang="en-US">"""+ output + 
            """ </lang></voice></speak>"""
        },
        'card': {
            'type': 'Simple',
            'title':  title,
            'content':  output
        },
        'reprompt': {
            'outputSpeech': {
                'type': 'PlainText',
                'text': reprompt_text
            }
        },
        'shouldEndSession': should_end_session
    }
    
def build_speechlet_response_music1(title, output, reprompt_text, should_end_session):
    return {
        'outputSpeech': {
            "type": "SSML",
            "ssml": """<speak> <audio src="soundbank://soundlibrary/magic/amzn_sfx_fairy_sparkle_chimes_01"/> <voice name="Brian"><lang xml:lang="en-GB">"""+ output + 
            """ </lang> </voice></speak>"""
        },
        'card': {
            'type': 'Simple',
            'title':  title,
            'content':  output
        },
        'reprompt': {
            'outputSpeech': {
                'type': 'PlainText',
                'text': reprompt_text
            }
        },
        'shouldEndSession': should_end_session
    }
    
def build_speechlet_response_music(title, output, reprompt_text, should_end_session):
    return {
        'outputSpeech': {
            "type": "SSML",
            "ssml": """<speak> <audio src="soundbank://soundlibrary/magic/amzn_sfx_fairy_sparkle_chimes_01"/> """+ output + 
            """ </speak>"""
        },
        'card': {
            'type': 'Simple',
            'title':  title,
            'content':  output
        },
        'reprompt': {
            'outputSpeech': {
                'type': 'PlainText',
                'text': reprompt_text
            }
        },
        'shouldEndSession': should_end_session
    }

def build_speechlet_response_music4(title, output, reprompt_text, should_end_session):
    return {
        'outputSpeech': {
            "type": "SSML",
            "ssml": """<speak> <audio src="soundbank://soundlibrary/magic_spells/magic_spells_03"/> <voice name="Brian"><lang xml:lang="en-GB">"""+ output + 
            """ </lang></voice>	</speak>"""
        },
        'card': {
            'type': 'Simple',
            'title':  title,
            'content':  output
        },
        'reprompt': {
            'outputSpeech': {
                'type': 'PlainText',
                'text': reprompt_text
            }
        },
        'shouldEndSession': should_end_session
    }

def build_speechlet_response_music5(title, output, reprompt_text, should_end_session):
    return {
        'outputSpeech': {
            "type": "SSML",
            "ssml": """<speak> <audio src="soundbank://soundlibrary/ui/gameshow/amzn_ui_sfx_gameshow_positive_response_02"/>"""+ output +
            """ <audio src="soundbank://soundlibrary/ui/gameshow/amzn_ui_sfx_gameshow_outro_01"/> </speak>"""

        },
        'card': {
            'type': 'Simple',
            'title':  title,
            'content':  output
        },
        'reprompt': {
            'outputSpeech': {
                'type': 'PlainText',
                'text': reprompt_text
            }
        },
        'shouldEndSession': should_end_session
    }
    
def build_speechlet_response_music6(title, output, reprompt_text, should_end_session):
    return {
        'outputSpeech': {
            "type": "SSML",
            "ssml": """<speak> <audio src="soundbank://soundlibrary/musical/amzn_sfx_musical_drone_intro_02"/>"""+ output +
            """ </speak>"""

        },
        'card': {
            'type': 'Simple',
            'title':  title,
            'content':  output
        },
        'reprompt': {
            'outputSpeech': {
                'type': 'PlainText',
                'text': reprompt_text
            }
        },
        'shouldEndSession': should_end_session
    }
    
def build_speechlet_response_music7(title, output, reprompt_text, should_end_session):
    return {
        'outputSpeech': {
            "type": "SSML",
            "ssml": """<speak> <audio src="soundbank://soundlibrary/sports/crowds/crowds_12"/>"""+ output +
            """ </speak>"""

        },
        'card': {
            'type': 'Simple',
            'title':  title,
            'content':  output
        },
        'reprompt': {
            'outputSpeech': {
                'type': 'PlainText',
                'text': reprompt_text
            }
        },
        'shouldEndSession': should_end_session
    }
    

def build_speechlet_response_music8(title, output, reprompt_text, should_end_session):
    return {
        'outputSpeech': {
            "type": "SSML",
            "ssml": """<speak> <audio src="soundbank://soundlibrary/human/amzn_sfx_crowd_boo_02"/>"""+ output +
            """ </speak>"""

        },
        'card': {
            'type': 'Simple',
            'title':  title,
            'content':  output
        },
        'reprompt': {
            'outputSpeech': {
                'type': 'PlainText',
                'text': reprompt_text
            }
        },
        'shouldEndSession': should_end_session
    }
    


def build_response(session_attributes, speechlet_response):
    return {
        'version': '1.0',
        'sessionAttributes': session_attributes,
        'response': speechlet_response
    }


# --------------- Functions that control the skill's behavior -----------------


def get_help_response():
    session_attributes = {}
    card_title = "Help"
    speech_output = """
    These are some of the commands, for you. To get started with puzzle drizzle.
    Say. Let's play. To start a new puzzle game.
    Say. Magic world. To learn magic tricks.
    Say. teach me. To make alexa to teach you a skill.
    """
    reprompt_text = "Say help me. To listen to the basic commands again"
    should_end_session = False
    
    return build_response(session_attributes, build_speechlet_response_music6(
        card_title, speech_output, reprompt_text, should_end_session))
        
def start_game(intent, session):
    points = 0
    session_attributes = {"points": points}
    card_title = "Start Game"
    speech_output = """
    There are three levels of questions in this game. Easy level. Medium level. Hard level.
     Please, select a question level.
    """
    reprompt_text = """
    There are three levels of questions in this game. Easy level. Medium level. Hard level.
     Select a question level.
    """
    should_end_session = False
    
    return build_response(session_attributes, build_speechlet_response(
        card_title, speech_output, reprompt_text, should_end_session))
    
def choose_level(intent, session):
    tempp = intent['slots']['difficulty']['value']
    answer = " "
    ques = " "
    card_title = "Welcome"
    points = 0
    if session.get('attributes', {}):
        points = session['attributes']['points']
        if tempp.lower() == 'easy':
            temp = random.choice(easy)
            ques = temp[0]
            answer = temp[1]
        
        elif tempp.lower() == 'medium':
            temp = random.choice(medium)
            ques = temp[0]
            answer = temp[1]
            
        elif tempp.lower() == 'hard':
            temp = random.choice(hard)
            ques = temp[0]
            answer = temp[1]
        
        else:
            start_game(intent, session)
        
    speech_output = ques
    reprompt_text = None
    session_attributes = {"answer":answer, "question":ques, "points":points}
    should_end_session = False

    return build_response(session_attributes, build_speechlet_response_music6(
        card_title, speech_output, reprompt_text, should_end_session))
    
compliments = [" Getting better! ", " Good! ", " Very good! ", " Excellent !", " Brilliant! ", " Awesome! "," Unstoppable! "]
insults = [" Better luck next time! "," Keep trying! ", " Come on! ", " You can do better! ", " It was a rare mistake. Not a problem "]
        
def answer_verification(intent, session):
    card_title = "Answer Checking"
    userans = intent['slots']['answer']['value']
    points = session['attributes']['points']
    if session.get('attributes', {}):
        item = session['attributes']['answer']
        if int(userans) == item:
            points += 20
            i = 0
            if points < 10:
                i = 0
            elif 10 <= points < 30:
                i = 1
            elif 30 <= points < 50:
                i = 2
            elif 50 <= points < 70:
                i = 3
            elif 70 <= points < 90:
                i = 4
            elif 90 <= points < 110:
                i = 5
            elif 110 <= points:
                i = 6
            speech_output = " Hey! You are" + compliments[i] +". You have " + str(points) + " points as of now. For next question . Say next question."
            reprompt_text = "Correct Answer"
            answer = session['attributes']['answer']
            ques = session['attributes']['question']
            session_attributes = {"answer":answer, "question":ques, "points":points}
            should_end_session = False
        
            return build_response(session_attributes, build_speechlet_response_music7(
                card_title, speech_output, reprompt_text, should_end_session))
        else:
            points -= 5
            i = 0
            if points < -20:
                i = 0
            elif -20 <= points < 0:
                i = 1
            elif 0 <= points < 30:
                i = 2
            elif 30 <= points < 60:
                i = 3
            elif 60 <= points < 90:
                i = 4
            elif 90 <= points:
                i = 5
            prompt = "Thats wrong." + " correct answer is " + str(item) + "." + insults[i] + ". You have " +str(points) + " points as of now. " +"For next question . Say next question."
            speech_output = prompt
            reprompt_text = prompt
            answer = session['attributes']['answer']
            ques = session['attributes']['question']
            session_attributes = {"answer":answer, "question":ques, "points":points}
            should_end_session = False

            return build_response(session_attributes, build_speechlet_response_music8(
                card_title, speech_output, reprompt_text, should_end_session))
    
    
 
def repeat_question(intent, session):
    ques = session['attributes']['question']
    card_title = "Repeat question"
    speech_output = ques
    reprompt_text = ques
    answer = session['attributes']['answer']
    ques = session['attributes']['question']
    points = session['attributes']['points']
    session_attributes = {"answer":answer, "question":ques, "points":points}
    should_end_session = False
    
    return build_response(session_attributes, build_speechlet_response_music3(
        card_title, speech_output, reprompt_text, should_end_session))       
        
def next_question(intent, session):
    card_title = "Start Game"
    speech_output = """
    Select a question level again. Easy level. Medium level. Hard level.
    """
    reprompt_text = """
    There are five levels of questions in this game. Beginner level. Easy level. Medium level. Hard level. And. Very hard level.
    Select a question level.
    """
    if session.get('attributes', {}):
        temp = session['attributes']["points"]
        session_attributes = {"points": temp}
    should_end_session = False
    return build_response(session_attributes, build_speechlet_response_music3(
        card_title, speech_output, reprompt_text, should_end_session))
    
def magic_world(intent, session):
    session_attributes = {}
    card_title = "Magic World"
    speech_output = """
                    Hey! Welcome to Magic world. This would be exciting.
                    First i will play a trick on you.
                    To learn. Say teach me, then i will teach you.
                    Incase my trick isn't attractive then you can say Next trick.
                    
                    Start learning tricks by saying start magic.
                    """
    reprompt_text = """
                    Hey! I said. Welcome to Magic world. First i will play a trick on you.
                    To learn. Say teach me, then i will teach you.
                    Start learning tricks by saying start learning.
                    """
    should_end_session = False

    return build_response(session_attributes, build_speechlet_response_music2(
        card_title, speech_output, reprompt_text, should_end_session))
        
    
def start_magic(intent, session):
  
    card_title = "Magic trick"
    trick = random.choice(tricks)
    speech_output = "Magic trick " + trick[0] + ". " + trick[1] + ". To learn this. Say. Teach me!"
    reprompt_text = "This is " + trick[0] + " " + trick[1]
    should_end_session = False
    session_attributes = {"choice": trick}

    return build_response(session_attributes, build_speechlet_response_music1(
        card_title, speech_output, reprompt_text, should_end_session))
    
     
def teach_magic(intent, session):
    card_title = "Teaching"
    if session.get('attributes', {}):
        trick = session['attributes']["choice"]
        speech_output = trick[2] + ". Say next trick to get new trick"
        reprompt_text = trick1[2] +  ". Say next trick to get new trick"
        session_attributes = {"choice": trick}
    
    should_end_session = False
    return build_response(session_attributes, build_speechlet_response_music4(
        card_title, speech_output, reprompt_text, should_end_session))
        
def by_number(intent, session):
    card_title = "Teaching"
    number = intent['slots']['trick']['value']
    trick = tricks[int(number) - 1]
    speech_output = trick[1]
    reprompt_text = trick1[1]
    session_attributes = {"choice": trick}
    should_end_session = False
    
    return build_response(session_attributes, build_speechlet_response_music4(
        card_title, speech_output, reprompt_text, should_end_session))
   
def get_welcome_response():
    session_attributes = {}
    card_title = "Welcome"
    speech_output = """
    Hey! Welcome to Puzzle Drizzle. Say let's play to start puzzle game.
    Or say magic world. To get into magic world.
    """
    reprompt_text = "I don't know if you heard me, welcome to Puzzle drizzle!. Say let's play to start a new game."
    should_end_session = False

    return build_response(session_attributes, build_speechlet_response_music(
        card_title, speech_output, reprompt_text, should_end_session))
        
def handle_session_end_request():
    card_title = "Session Ended"
    speech_output = """
    Thank you for playing puzzle drizzle. Hope you liked it!
    Have a nice day! """
    should_end_session = True
    
    return build_response({}, build_speechlet_response_music5(
        card_title, speech_output, None, should_end_session))


# --------------- Events ------------------

def on_session_started(session_started_request, session):
    """ Called when the session starts.
        One possible use of this function is to initialize specific 
        variables from a previous state stored in an external database
    """
    # Add additional code here as needed
    pass

    

def on_launch(launch_request, session):
    return get_welcome_response()


def on_intent(intent_request, session):
    """ Called when the user specifies an intent for this skill """
    points = 0
    answer = " "
    intent = intent_request['intent']
    intent_name = intent_request['intent']['name']

    # Dispatch to your skill's intent handlers
    
    
    if intent_name == "StartGameIntent":
        return start_game(intent, session)
    elif intent_name == "LevelIntent":
        return choose_level(intent, session)
    elif intent_name == "AnswerIntent":
        return answer_verification(intent, session)
    elif intent_name == "AMAZON.NextIntent":
        return next_question(intent, session)
    elif intent_name == "AMAZON.RepeatIntent":
        return repeat_question(intent, session)
    elif intent_name == "MagicWorldIntent":
        return magic_world(intent, session)
    elif intent_name == "TeachMagicIntent":
        return teach_magic(intent, session)
    elif intent_name == "ByNumberIntent":
        return by_number(intent, session)
    elif intent_name == "StartMagicIntent":
        return start_magic(intent, session)
    elif intent_name == "AMAZON.HelpIntent":
        return get_help_response()
    elif intent_name == "AMAZON.CancelIntent" or intent_name == "AMAZON.StopIntent":
        return handle_session_end_request()
    else:
        raise ValueError("Invalid intent")
        


def on_session_ended(session_ended_request, session):
    """ Called when the user ends the session.
    Is not called when the skill returns should_end_session=true
    """
    print("on_session_ended requestId=" + session_ended_request['requestId'] +
          ", sessionId=" + session['sessionId'])
    # add cleanup logic here



def lambda_handler(event, context):

    print("Incoming request...")

    # if (event['session']['application']['applicationId'] !=
    #         "amzn1.echo-sdk-ams.app.[amzn1.ask.skill.032b2028-684d-4f00-9d69-e3182aaf36e1]"):
    #     raise ValueError("Invalid Application ID")

    if ('session' in event):
        print("event.session.application.applicationId=" +
              event['session']['application']['applicationId'])
        if event['session']['new']:
            on_session_started({'requestId': event['request']['requestId']},
                           event['session'])
                           
    if ('request' in event):                       
        if event['request']['type'] == "LaunchRequest":
            return on_launch(event['request'], event['session'])
        elif event['request']['type'] == "IntentRequest":
            return on_intent(event['request'], event['session'])
        elif event['request']['type'] == "SessionEndedRequest":
            return on_session_ended(event['request'], event['session'])