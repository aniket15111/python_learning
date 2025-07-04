class BatchIterator:
    def __init__(self, data, batch_size):
        self.data = data
        self.batch_size = batch_size
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.data):
            raise StopIteration
        batch = self.data[self.index : self.index + self.batch_size]
        self.index += self.batch_size
        return batch


data = [1, 2, 3, 4, 5, 6, 7]
batcher = BatchIterator(data, 3)

for batch in batcher:
    print(batch)
