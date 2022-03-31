try:
    word = ["Everything is half here,",
            "like the marble head",
            "of the Roman emperor",
            "and the lean torso",
            "of his favorite.",
            "The way the funnel cloud",
            "which doesn't seem",
            "to touch ground does—",
            "flips a few cars, a semi—",
            "we learn to..."
            ]
    with open('dd$i.txt', 'x') as fw:
        fw.write('\n'.join(word))
except:
    print("You must have \"FileAlreadyExist\" exception handling")
