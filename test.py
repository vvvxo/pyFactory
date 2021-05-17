import matplotlib.pyplot as plt
import matplotlib.patches as patches
import setFactory as set

fig, ax = plt.subplots()
ax.plot([1, 4], [1, 4])


def add_rectangle(area, xy):
    print(area, xy)
    ax.add_patch(
        patches.Rectangle(
            (xy[0] - area[0] / 2, xy[1] - area[1] / 2),
            area[0],
            area[1],
            edgecolor='blue',
            facecolor='red',
            fill=False)
        #     (area[0] - xy[0] / 2, area[1] - xy[1] / 2)),
        # width=xy[0], height=xy[1], edgecolor='blue',
        # facecolor='red',
    )


def show_image():
    plt.show()
