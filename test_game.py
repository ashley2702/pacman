import unittest
from maze import Maze
from pacman import PacMan
from ghost import Ghost

class TestPacManGame(unittest.TestCase):
    def setUp(self):
        self.maze = Maze()
        self.pacman = PacMan(1, 1)
        self.ghost = Ghost(10, 3, "Blinky")

    def test_pacman_movement(self):
        
    # Move right (valid move)
            self.pacman.move("right", self.maze)
            self.assertEqual((self.pacman.x, self.pacman.y), (2, 1))  # Correct based on maze layout

    # Move down (valid move)
            self.pacman.move("down", self.maze)
            self.assertEqual((self.pacman.x, self.pacman.y), (2, 2))  # Should reach (2, 2)

    # Attempt to move into a wall
            self.pacman.move("left", self.maze)  # Assume wall to the left
            self.assertEqual((self.pacman.x, self.pacman.y), (2, 2))  # Should not move


    def test_dot_collection(self):
        # Place a dot and test collection
        self.maze.place_dot(2, 1)
        self.pacman.move("right", self.maze)
        self.assertEqual(self.pacman.score, 10)

    def test_ghost_movement(self):
        # Test ghost stays within valid positions
        original_position = (self.ghost.x, self.ghost.y)
        self.ghost.move(self.maze)
        self.assertNotEqual((self.ghost.x, self.ghost.y), original_position)
        self.assertFalse(self.maze.is_wall(self.ghost.x, self.ghost.y))

if __name__ == "__main__":
    unittest.main()
