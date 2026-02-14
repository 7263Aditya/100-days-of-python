def calculate_love_score(name1, name2):
    # Convert both names to lowercase
    name1 = name1.lower()
    name2 = name2.lower()
    
    # Combine both names into one string
    combined_names = name1 + name2

    # Define the words TRUE and LOVE
    word_true = "true"
    word_love = "love"

    # Count the occurrences of each letter in TRUE
    true_count = sum(combined_names.count(letter) for letter in word_true)

    # Count the occurrences of each letter in LOVE
    love_count = sum(combined_names.count(letter) for letter in word_love)

    # Combine the counts to form the love score
    love_score = int(f"{true_count}{love_count}")

    # Print the love score
    print(love_score)

    # Return the love score
    return love_score
calculate_love_score("Kanye West","Kim Kardashian")