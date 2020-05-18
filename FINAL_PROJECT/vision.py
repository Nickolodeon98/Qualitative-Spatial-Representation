import matplotlib.pyplot as plt
import main

def plot(A, color):
    A_x = [A.a.x, A.b.x, A.c.x, A.d.x, A.a.x]
    A_y = [A.a.y, A.b.y, A.c.y, A.d.y, A.a.y]
    # B_x = [B.a.x, B.b.x, B.c.x, B.d.x, B.a.x]
    # B_y = [B.a.y, B.b.y, B.c.y, B.d.y, B.a.y]

    plt.figure(main.num)
    plt.axis([0, 20, 0, 20])
    plt.plot(A_x, A_y, lw=1, color=f'{color}', label=f'Region {A.name}')
    # plt.plot(B_x, B_y, lw=2, color='red', label='Region B')
    plt.pause(0.0001)

def draw():
    plt.axhline(0, lw=0.5, color='black')
    plt.axvline(0, lw=0.5, color='black')
    plt.legend()
    plt.show(block=False)
    plt.ion()
    plt.pause(0.0001)
    plt.legend()

def save():
    plt.savefig('plot', format='png')