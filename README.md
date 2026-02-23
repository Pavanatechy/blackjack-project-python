# Blackjack Game

A simple command-line implementation of the classic card game Blackjack in Python.

## Description

This is a playable blackjack game where you play against the computer. The goal is to get a hand value closer to 21 than the dealer without going over.

## Files

- **blackjack project.py** - Main game logic and gameplay
- **art.py** - ASCII art logo for the game

## How to Play

1. Run the game: `python "blackjack project.py"`
2. You'll be dealt 2 cards and the computer (dealer) will be dealt 2 cards
3. You can choose to hit (get another card) or stand (keep your current hand)
4. The computer will play according to standard blackjack rules
5. Highest hand value under 21 wins!

## Game Rules

- Number cards are worth their face value
- Face cards (J, Q, K) are worth 10
- Aces are worth 11 or 1 (automatically adjusted to prevent busting)
- Blackjack (21 on first 2 cards) beats regular 21
- Going over 21 means you lose ("bust")

## Requirements

- Python 3.x

Enjoy the game!
