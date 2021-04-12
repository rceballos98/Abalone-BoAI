from hexalattice import hexalattice as hexa
from matplotlib import pyplot as plt
import numpy as np

def plot_game(game):
   
    hex_centers, h_ax = hexa.create_hex_grid(nx=9, ny=9, min_diam=1, do_plot=False)
    tile_centers_x = hex_centers[:, 0]
    tile_centers_y = hex_centers[:, 1]
    color_shape = (len(hex_centers), 4)

    indexes = [
        list(range(2,7)),
        list(range(10,16)),
        list(range(19,26)),
        list(range(27,35)),
        list(range(36,45)),
        list(range(45,53)),
        list(range(55,62)),
        list(range(64,70)),
        list(range(74,79)),
    ]

    edge_in_board = np.hstack(np.array([0,0,0,0.2]))
    edge_out_board = np.hstack(np.array([1,1,1,0]))
    edge_in_board_occupuied =np.hstack(np.array([0,0,0,1]))

    black_piece = np.hstack(np.array([0,0,0,1]))
    white_piece = np.hstack(np.array([1,1,1,1]))
    blank_piece = np.hstack(np.array([0,0,0,0.2]))


    # Define edge colors
    new_edge_colors = np.zeros(color_shape)
    new_edge_colors[:,:] = edge_out_board
    new_edge_colors[np.hstack(indexes)] = edge_in_board

    # Define Face colors
    new_face_colors = np.zeros(color_shape)
    for game_piece, index in zip(np.hstack(game.board), np.hstack(indexes)):
        if game_piece.value == 1:
            new_face_colors[index] = black_piece
            new_edge_colors[index] = edge_in_board_occupuied
        elif game_piece.value == 0:
            new_face_colors[index] = blank_piece
        elif game_piece.value == -1:
            new_face_colors[index] = white_piece
            new_edge_colors[index] = edge_in_board_occupuied
        else:
            raise ValueError(f'Unknown game piece value:{game_piece.value}')

    ax_handler = hexa.plot_single_lattice_custom_colors(hex_centers[:, 0], hex_centers[:, 1],
                                face_color=new_face_colors,
                                edge_color=new_edge_colors,
                                min_diam=0.95,
                                plotting_gap=0.05,
                                rotate_deg=0,
                                )
    ax_handler.axes.xaxis.set_visible(False)
    ax_handler.axes.yaxis.set_visible(False)
    
    return ax_handler