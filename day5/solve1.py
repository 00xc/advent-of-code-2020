from multiprocessing import Pool

ROWS = list(range(128))
COLS = list(range(8))

def get_row(text, rows=ROWS):
	if len(text) == 0: return rows[0]
	if text[0] == "B": return get_row(text[1:], rows[len(rows)//2:])
	elif text[0] == "F": return get_row(text[1:], rows[:len(rows)//2])

def get_col(text, cols=COLS):
	if len(text) == 0: return cols[0]
	if text[0] == "R": return get_col(text[1:], cols[len(cols)//2:])
	elif text[0] == "L": return get_col(text[1:], cols[:len(cols)//2])

def worker(inp):
	row = get_row(inp[:7])
	col = get_col(inp[7:])
	return row*8 + col

if __name__ == '__main__':

	with Pool(4) as pool:
		with open("input.txt", "r") as f:
			res = pool.map(worker, [line.rstrip() for line in f.readlines()])

	print(max(res))

