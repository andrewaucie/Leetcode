class Solution():
    def fullJustify(self, words, maxWidth):
        result = []
        line = []
        line_length = 0
        
        for word in words:
            if line_length + len(line) + len(word) > maxWidth:
                # Justify the current line
                spaces_to_add = maxWidth - line_length
                if len(line) == 1:
                    result.append(line[0] + ' ' * spaces_to_add)
                else:
                    num_gaps = len(line) - 1
                    spaces_per_gap = spaces_to_add // num_gaps
                    extra_spaces = spaces_to_add % num_gaps
                    justified_line = line[0]
                    for i in range(1, len(line)):
                        spaces = spaces_per_gap + (1 if i <= extra_spaces else 0)
                        justified_line += ' ' * spaces + line[i]
                    result.append(justified_line)
                
                # Reset line and line_length
                line = []
                line_length = 0
            
            line.append(word)
            line_length += len(word)
        
        # Left-justify the last line
        last_line = ' '.join(line)
        last_line += ' ' * (maxWidth - len(last_line))
        result.append(last_line)
        
        return result