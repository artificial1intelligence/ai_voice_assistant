"""
This file process converted text and perform actions accordingly.
This file can be extended with more action.
"""
import valib as va
import action as a
import time
import logging

logger = logging.getLogger('voice assistant')


def process_text(text, pa):

    """
    asking who are you?
    """
    if "who are you" in text:
        va.audio_playback("i am a i voice assistant system")

    """
    asking about weather information.
    """
    if "weather" in text:
        va.audio_playback("which city")
        time.sleep(0.5)
        file_name = pa.process(3)
        city = pa.voice_command_processor(file_name)
        logger.info("process_text : City :: " + city)
        try:
            humidity, temp, phrase = a.weatherReport(city)
            va.audio_playback(
                "currently in " + city + " temperature is " + str(temp) + " degree celsius, " + "humidity is " + str(
                    humidity) + " percent and sky is " + phrase)
            logger.info("currently in " + city + " temperature is " + str(temp) + "degree celsius, " + "humidity is " + str(
                humidity) + " percent and sky is " + phrase)
        except KeyError as e:
            va.audio_playback("sorry, i couldn't get the location")

            
    """
    asking for search somthing like:
    what is raspberry pi
    who is isac newton etc.
    """
    if "search" in text or "Search" in text:
        va.audio_playback("tell me what to search")
        time.sleep(0.5)
        file_name = pa.process(5)
        search_data = pa.voice_command_processor(file_name)
        try:
            result = a.google_search(search_data)
            if result:
                va.audio_playback(result)
            else:
                va.audio_playback("sorry, i couldn't find any result for " + search_data)
        except KeyError as e:
            va.audio_playback("sorry, i couldn't find any result for " + search_data)
            
            pass
        
        
      elif "let's play" in result["text"]:
            a22=["stone",'paper','scissor']
            print("let's play")
            va.audio_playback("ok , let's play ,    stone, paper and scissor.  i will chose")
            rand = random.choice(a22)
            va.audio_playback(rand)
            

        if "stone" in text:
            a1=['paper','scissor','stone']
            rand = random.choice(a1)
            va.audio_playback(rand)
            
        if "paper" in text:
            a2 = ['paper', 'scissor', 'stone']
            rand = random.choice(a2)
            va.audio_playback(rand)
            
        if "scissor" in text:
            a3 = ['paper', 'scissor', 'stone']
            rand = random.choice(a3)
            va.audio_playback(rand)
            
        if "joke" in text:
        va.audio_playback(pyjokes.get_joke())
                  
          

        
    """
    asking aboout current time.
    """
    if "time" in text or "Time" in text:
        current_time = a.current_datetime("time")
        va.audio_playback("right now it is " + current_time)

    """
    asking about today's date.
    """
    if "date" in text or "Date" in text:
        date = a.current_datetime("date")
        va.audio_playback("today it is " + date)

        
    """
    asking for rebooting the voice assistant system.
    """
    if "reboot" in text or "Reboot" in text:
        va.audio_playback("ok.. rebooting the server")
        a.reboot_server()

    return "done"
