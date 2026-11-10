# %%
records = 250
failed = 38
passed = records - failed
failed_percentage = (failed / records) * 100
passed_percentage = (passed / records) * 100
# %%
def greet():
    print("Hello, welcome to the program!")    
    
# %%
def shout(word):
    print(word.upper() + "!!!")
shout(word)
shout(word)
    
# %%
