----------------------------------------------
Below are listed the use AI tools by sections and source
----------------------------------------------

------------------------------
Setup.py
------------------------------
- Claude Sonnet 3.5 used to understand why the code was not recognizing already installed packages.
  - Prompt: "I have the yfinance library installed but according to code it says it is not installed"
- ChatGPT 5.0 used to spot mistake in the pip upgrader. 
  - Prompt : why does my function does not upgrade correctly the package ? subprocess.check_call([sys.executable, "-","pip", "install",f"{name}=={version}", "--upgrade" ])