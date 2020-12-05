
import math

input_lines = open("/Users/ciaran.whyte/dev/aoc2020/day5/input.txt").read()
# input_lines = """BFFFBBFRRR
# FFFBBBFRRR
# BBFFBBFRLL
# """

MAX_ROW=127
MIN_ROW=0

MAX_COL=7
MIN_COL=0

plane_map = { a: [i for i in range(8)] for a in range(128) }

def get_seat_id(boarding_pass: str)-> int:
    row_path=boarding_pass[:7]
    col_path=boarding_pass[7:]

    c_row_max=MAX_ROW
    c_row_min=MIN_ROW
    for r in row_path:        
        if r == 'F':
            c_row_max -= math.floor((c_row_max-c_row_min)/2) + 1
        else:
            c_row_min += math.ceil((c_row_max-c_row_min)/2)
        # print(f"{c_row_min} {c_row_max}")
    
    c_col_max=MAX_COL
    c_col_min=MIN_COL
    for c in col_path:        
        if c == 'L':
            c_col_max -= math.floor((c_col_max-c_col_min)/2) + 1
        else:
            c_col_min += math.ceil((c_col_max-c_col_min)/2)
        # print(f"{c_col_min} {c_col_max}")

    plane_map[c_row_min][c_col_min]= 'X'
    return c_row_min * 8  + c_col_min

max_seat_id=0
for boarding_pass in input_lines.splitlines():
    seat_id = get_seat_id(boarding_pass)
    # print(f"boarding_pass: {boarding_pass} => seat_id {seat_id}")
    max_seat_id=max(max_seat_id, seat_id)

print(f"Part 1: {max_seat_id}")

for row in plane_map:
    # print(f"{row} : {plane_map[row]}") 
    if len(set(plane_map[row])) == 2:
        # print(f"{row} : {plane_map[row]}") 
        for seat in plane_map[row]:
            if seat != 'X':
                if seat-1 >= 0:
                    seat_minus_one = plane_map[row][seat-1]
                else:
                    seat_minus_one = plane_map[row-1][7]

                seat_number =  plane_map[row][seat]

                if seat+1 <= 7:
                    seat_plus_one = plane_map[row][seat+1]
                else:
                    seat_plus_one = plane_map[row+1][0]
                
                if seat_plus_one == 'X' and seat_minus_one == 'X':
                    print(f"Part 2: {row * 8 + seat_number}")
                    exit(0)
 


                








