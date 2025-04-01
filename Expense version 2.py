import argparse
import json
import datetime

#all json entries should have ID, Date, Description, Amount

filepath = "Type 3.json"


def main():
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers(dest="command", required=True)
    subparsers.required = True

    add_parser = subparsers.add_parser("add", help="create a new object")
    add_parser.add_argument("-d", "--description", required=True, help="description of the object")
    add_parser.add_argument("-c", "--cost", type=float, required=True, help="cost of the object")

    args = parser.parse_args()


    if args.command == "add":
        print(f"Creating a new object with description: {args.description} and cost: {args.cost}")
        with open(filepath, "r") as file:
            data = json.load(file)
            if not data:
                new_id = 1
            else:
                new_id = data[-1]["id"] + 1
            current_date = datetime.datetime.now().strftime("%Y-%m-%d")
        new_object = {
            "id": new_id,
            "date": current_date,
            "description": args.description,
            "cost": args.cost
        }
        data.append(new_object)
        with open(filepath, "w") as file:
            json.dump(data, file, indent=4)
        print(f"New object created with ID: {new_id}")



if __name__ == "__main__":
    main()
