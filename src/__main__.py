if __name__ == "__main__":
    import sys
    sys.path.append(sys.path[0] + "\\src")
    print(sys.path)

    from src import game
    game.run_game()