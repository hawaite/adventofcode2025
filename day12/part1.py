from rectpack import newPacker

def main():
    with(open("./input.txt", "r")) as fp:
        lines = map(str.strip,fp.readlines())

    input_file_shape_areas = [7, 7, 6, 5, 7, 7]

    lazy_packing_possibe = 0
    potentially_possible = 0
    definitely_not_possible = 0

    for line in lines:
        if "x" in line:
            box_dimiensions, shape_counts = line.split(": ")
            w,h = map(int,box_dimiensions.split("x"))
            shape_list = list(map(int, shape_counts.split(" ")))
            total_shapes = sum(shape_list)
            bounding_boxes = [(3,3)] * total_shapes

            packer = newPacker()
            for r in bounding_boxes:
                packer.add_rect(*r)
            
            packer.add_bin(w,h)

            packer.pack()

            numer_packed_successfully_in_bin = len(packer[0])
            if numer_packed_successfully_in_bin == total_shapes:
                lazy_packing_possibe += 1
            else:
                # test if completely packed size would exceed area
                total_area = 0
                for shape_ix, shape_count in enumerate(shape_list):
                    total_area += (shape_count * input_file_shape_areas[shape_ix])

                if total_area > (w * h):
                    definitely_not_possible += 1
                else:
                    potentially_possible += 1


    
    print(f"definitely possible with lazy packing: {lazy_packing_possibe}")
    print(f"definitely not possible even with complete packing: {definitely_not_possible}")
    print(f"potentially possible: {potentially_possible}")
    # The joke here is that the input was crafted such that the shapes dont matter
    # every line can be either lazy bin-packed using its 3x3 bounding box
    # or the sum of the area of all the shapes exceed the box area, meaning it couldnt
    # be packed even if it was 100% dense.

if __name__ == "__main__":
    main()