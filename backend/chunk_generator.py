def generate_chunks(
    snippets,
    chunk_size=500
):

    chunks = []

    for snippet in snippets:

        text = snippet["snippet"]

        for i in range(
            0,
            len(text),
            chunk_size
        ):

            chunks.append(
                {
                    "file":
                        snippet["file"],

                    "chunk":
                        text[
                            i:i+chunk_size
                        ]
                }
            )

    return chunks