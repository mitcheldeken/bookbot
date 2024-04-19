def main():
    path_to_file = "books/frankenstein.txt"
    with open(path_to_file) as f:
        file_contents = f.read()
    lower_file_contents = file_contents.lower()
    count_dict = {}
    for c in lower_file_contents:
        if c in count_dict:
            count_dict[c]+=1
        else:
            if c.isalpha():
                count_dict[c]=1
    dict_list = [{'character':character,'count':count_dict[character]} for character in count_dict]

    def sort_on(dict):
        return dict["count"]

    dict_list.sort(reverse=True, key=sort_on)

    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{len(file_contents.split())} words found in the document\n")
   
    for entry in dict_list:
        print(f"The '{entry['character']}' character was found {entry['count']} times")
    print("--- End report ---")
if __name__ == "__main__":
    main()


