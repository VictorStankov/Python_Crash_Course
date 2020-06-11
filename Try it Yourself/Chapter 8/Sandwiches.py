def build_sandwich(*stuff):
    print("\nMaking a sandwich with the following ingredients:")
    for thing in stuff:
        print("- " + thing)


build_sandwich('cheese')
build_sandwich('cucumber', 'cheese')
build_sandwich('tomato', 'egg', 'cheese')