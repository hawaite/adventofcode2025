from rectpack import newPacker

def main():
    with(open("./input.txt", "r")) as fp:
        lines = map(str.strip,fp.readlines())

    # all the shapes in the example and full input are all 3x3
    lazy_packing_possibe = 0
    for line in lines:
        if "x" in line:
            box_demiensions, shape_counts = line.split(": ")
            w,h = map(int,box_demiensions.split("x"))

            total_shapes = sum(map(int, shape_counts.split(" ")))
            bounding_boxes = [(3,3)] * total_shapes

            packer = newPacker()
            for r in bounding_boxes:
                packer.add_rect(*r)
            
            packer.add_bin(w,h)

            packer.pack()

            numer_packed_successfully_in_bin = len(packer[0])
            if numer_packed_successfully_in_bin == total_shapes:
                lazy_packing_possibe += 1
    
    print(f"lazy packing possible: {lazy_packing_possibe}")

if __name__ == "__main__":
    main()