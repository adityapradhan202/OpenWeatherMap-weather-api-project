import coordinates_india as cind
import api_request_response as ap

def home_page():
    try:
        print("Currently our program is only able to tell the current time weather of states of India!")
        city_name = input("Enter the name of the city: ")
        city_name = city_name.title()

        lat = cind.capital_coordinates[city_name][0]
        long = cind.capital_coordinates[city_name][1]

        ap.give_weather(lat, long, ap.api_key)

    except:
        print("Some error occured!")
    finally:
        user_input = input("If you want to know the weather of some other state then enter 'y' otherwise 'n': ")
        
        if user_input.lower() == "y":
            home_page()
        elif user_input.lower() == "n":
            print("\nThank you for using our weather service!")
            exit(0)
        else:
            print("Invalid input!\n")
            home_page()


def main():
    home_page()

if __name__ == "__main__":
    main()