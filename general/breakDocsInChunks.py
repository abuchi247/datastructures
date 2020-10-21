# A document is stored in the cloud and you need to send the text of the document to the client
# which renders it on the screen.
# We want to send the document in chunk by chunk based on the below constraints

# RULES
# 1. A chunk can be 5000 or fewer characters in length (is a relaxed rule only one condition (5))
# 2. A chunk should container only complete paragraphs - Hard and fast rule
# 3. A paragraph is represented by the ":" character in the document
# 4. List of chunks should be in the order they appear in the document (do not setup chunks out of order)
# 5. If you encounter a paragraph > 5000 characters should be in a separate chunk by itself
# 6. Get all the chunks as close to 5000 characters as possible based on the constraint above


def chunkify(doc, chunk_size = 5000):
    """
    Converts a string into chunks to be sent to client
    :param doc:
    :param chunk_size:
    :return:
    """
    DELIMITER = ":"
    paragraphs = doc.split(DELIMITER)   # gets all the paragraphs into a list

    chunks_list = []    # hold the chunk list
    current_chunk = ""  # store the current chunk

    for paragraph in paragraphs:
        # check if the current chunk and paragraph violates rule 2
        if len(current_chunk) + len(paragraph) > chunk_size:
            chunks_list.append(current_chunk)
            current_chunk = ""

        # check if the paragraph is part of rule 5
        if len(paragraph) > chunk_size:
            if len(current_chunk) > 0:
                chunks_list.append(current_chunk)
                current_chunk = ""
            chunks_list.append(paragraph + DELIMITER)
            continue

        current_chunk += paragraph + DELIMITER

    if len(current_chunk) > 0:
        chunks_list.append(current_chunk)

    return chunks_list


if __name__ == "__main__":
    documents = "a:bb:cc:abcdef:ab:c:d"

    chunks = chunkify(documents, 5)

    for chunk in chunks:
        print(chunk)