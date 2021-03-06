def is_consistent(tags, new_tag, num_tags):
    # 0 means open tag
    # 1 means closed tag
    if not tags and new_tag == "1":
        return False
    elif not tags and new_tag == "0":
        return True

    count_open = tags.count("0")
    count_open += 1 if new_tag == "0" else 0

    count_closed = tags.count("1")
    count_closed += 1 if new_tag == "1" else 0

    if count_closed > count_open or count_closed > num_tags or count_open > num_tags or count_closed + count_open > 2*num_tags:
        return False
    return True


def is_sol(tags, num_tags):
    return tags.count("0") == tags.count("1") and len(tags) == 2 * num_tags


def convert_num_tags_to_divs(tags):
    return "".join(["<div>" if tag == "0" else "</div>" for tag in tags])


def generate_tags(tags, sols, num_tags):
    for tag in "01":
        if is_consistent(tags, tag, num_tags):
            tags.append(tag)

            if is_sol(tags, num_tags):
                sols.append(convert_num_tags_to_divs(tags))

            generate_tags(tags, sols, num_tags)
            tags.pop()


def generateDivTags(numberOfTags):
    # Write your code here.
    sols = []
    generate_tags([], sols, numberOfTags)
    return sols


print(generateDivTags(1))
