class Solution:
    def calPoints(self, operations: List[str]) -> int:
        record = []

        for item in operations:
            if item == "+":
                last_item = record.pop()
                second_last_item = record.pop()

                record.append(second_last_item)
                record.append(last_item)
                record.append(second_last_item + last_item)

            elif item == "D":
                last_item = record.pop()
                record.append(last_item)
                record.append(last_item * 2)

            elif item == "C":
                record.pop()

            else:
                record.append(int(item))

    
        return sum(record)