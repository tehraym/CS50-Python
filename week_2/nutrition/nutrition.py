def main():
    fruit = input("Item: ")
    fruit = fruit.lower()
    match fruit:
        case "apple":
            print("Calories: 130")
        case "avocado":
            print("Calories: 50")
        case "banana":
            print("Calories: 110")
        case "cantaloupe":
            print("Calories: 50")
        case "grapefruit":
            print("Calories: 60")
        case "grapes":
            print("Calories: 90")
        case "honeydew melon":
            print("Calories: 50")
        case "kiwifruit":
            print("Calories: 90")
        case "lemon":
            print("Calories: 15")
        case "nectarine":
            print("Calories: 60")
        case "orange":
            print("Calories: 80")
        case "sweet cherries":
            print("Calories: 100")
        case "pear":
            print("Calories: 100")

main()