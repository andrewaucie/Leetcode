class Solution:
    def findDuplicate(self, paths):
        from collections import defaultdict

        # Dictionary to hold file content as key and list of file paths as value
        content_map = defaultdict(list)

        # Iterate over each path string
        for path in paths:
            # Split path into directory and files
            parts = path.split(' ')
            directory = parts[0]  # The root directory
            files = parts[1:]     # The files in the directory

            # Process each file
            for file in files:
                # Split file name and content
                filename, content = file.split('(')
                content = content[:-1]  # Remove the closing parenthesis

                # Construct the full file path
                full_path = f"{directory}/{filename}"
                # Map content to file path
                content_map[content].append(full_path)

        # Filter and collect paths with duplicate contents
        duplicates = [paths for paths in content_map.values() if len(paths) > 1]

        return duplicates
