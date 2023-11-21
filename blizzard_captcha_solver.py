import capsolver
from urllib.parse import urlparse

# Change this information
capsolver.api_key = "Your pay per usage key"

def solve_funcaptcha_blizzard():
    solution = capsolver.solve({
   "type": "FunCaptchaTaskProxyLess",
        "websiteURL": "https://eu.account.battle.net",
        "websitePublicKey": "CF5C61EE-F062-45DF-A32F-E9398E2B4E0D",
        "funcaptchaApiJSSubdomain": "https://blizzard-api.arkoselabs.com"
        
    })
    return solution

def main():
    
    print("Solving blizzard captcha")
    solution = solve_funcaptcha_blizzard()
    
    token = solution["token"]
    
    print("Token Solution " + token)
    
if __name__ == "__main__":
    main()
