import datetime

def main():
    birth_year = int(input("Entrer votre année de naissance : "))
    current_year = datetime.date.today().year
    age = current_year - birth_year

    print(f"votre age actuel est {age} ans")

if __name__ == "__main__":
    main()
