import requests # This is a lib that access things online
import hashlib # This is a lib that change value to glibberish value
import sys # This makes us to access the argv from the cmdline

def request_api_data(query_char): 
    url = "https://api.pwnedpasswords.com/range/" + query_char # This is >> "Have i been Pwned" API and with a hash generator password using SHA 1 
    res = requests.get(url)  # This is getting the API to work.
    if res.status_code != 200: # checking if api works
        raise RuntimeError(f"Error Fetching: {res.status_code}, check the api and try again")
    return res


# def read_res(response): # To learn more about the request func
#     print(response.text)
def get_password_leaks_count(hashes, hash_to_check): # This func recognize breach data
    hashes = (line.split(':') for line in hashes.text.splitlines()) # seperate hash data text using tuple comprehension
    for h, count in hashes: 
        if h == hash_to_check: 
            return count
    return 0


    
def check_pwned_api(password): # check if password is seen at pwned_api
    sha1password = hashlib.sha1(password.encode('utf-8')).hexdigest().upper() # This change value to hash value in a standard form.
    first_5, tail = sha1password[:5], sha1password[5:] # This seperate the hash value to pick the first 5(k-anonymities) to fit the request func
    response = request_api_data(first_5) # This brings the hash value to be seen.
    # return read_res(response) # This shows more values
    return get_password_leaks_count(response, tail) # seperated hash value



def main(args): # This func helps us to loop into the password given and other functions
    for password in args: 
        count = check_pwned_api(password)
        if count:
            print(f"{password} was found {count} times .... you should probably change your password")
        else: 
            print(f"{password} was Not found. Carry on!")
    return "done!"


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:])) # This access the value(password) in the sys cmdline
    
    