def get_ratings(names):
    ratings = {}
    for name in names:
        print(f"Hello, {name}! Let's rate your compatibility with others:")
        others_ratings = {}
        for other_name in names:
            if other_name != name:
                try:
                    rating = int(input(f"On a scale of 1 to 10, how much would you like to be in a room with {other_name}? "))
                    if 1 <= rating <= 10:
                        others_ratings[other_name] = rating
                    else:
                        print("Please enter a valid rating between 1 and 10.")
                except ValueError:
                    print("Invalid input. Please enter a numeric rating.")
        ratings[name] = others_ratings
    return ratings

def create_groups(names, group_size, ratings_dict):
    sorted_names = sorted(names, key=lambda x: sum(ratings_dict[x].get(other, 0) for other in names), reverse=True)
    groups = []
    while sorted_names:
        group = sorted_names[:group_size]
        groups.append(group)
        sorted_names = sorted_names[group_size:]
    return groups

def main():
    num_people = int(input("How many people are there? "))
    people_names = [input(f"Enter name {i+1}: ") for i in range(num_people)]
    ratings_dict = get_ratings(people_names)

    group_size = 3
    groups = create_groups(people_names, group_size, ratings_dict)

    print("\nOptimized groups:")
    for i, group in enumerate(groups, start=1):
        print(f"Group {i}: {', '.join(group)}")

if __name__ == "__main__":
    main()