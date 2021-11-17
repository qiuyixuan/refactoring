/**
*File: Board.java
*Author: Xiangxi Mu
*Date: 09/20/2020
 */
import java.awt.Graphics;
import java.io.*;
import java.util.Arrays;
import java.util.ArrayList;
import java.awt.Font;
public class Board{
    private Cell [][] grid;
    public static final int Size = 9;
    //default constructor
    public Board(){
        grid = new Cell [Board.Size][Board.Size];
        for ( int r = 0; r < Board.Size; r++){
            for ( int c = 0; c < Board.Size; c++){
                grid[r][c] = new Cell(r, c, 0);
            }
        }
    }
    public String toString(){
        String result = "";
        for ( int r = 0; r < Board.Size; r++){
            for (int c = 0; c < Board.Size; c++){
                result += grid[r][c].toString();
                if (c == 2 || c == 5){
                    result += "  ";
                }
            }
            result += "\n";
            if (r == 2 || r == 5){
                result += "\n";
            }
            
        }
        return result;
    }
    //This return the number of columns of the board
    public int getCols(){
        return this.Size;
    }
    //returns the number of rows of the board
    public int getRows(){
        return this.Size;
    }
    //returns the cell at position [r][c]
    public Cell get(int r, int c){
        return grid[r][c];
    }
    //returns if the cell in [r][c] is locked
    public boolean isLocked(int r, int c){
        return grid[r][c].isLocked();
    }
    //returns the number of locked cells on the board
    public int numLocked(){
        int result = 0;
        for (int r = 0; r < this.Size; r++){
            for (int c = 0; c < this.Size; c++){
                if (grid[r][c].isLocked() == true){
                    result += 1;
                }
            }
        }
        return result;
    }
    //returns the value at [r][c]
    public int value(int r, int c){
        return grid[r][c].getValue();
    }
    //it sets the value of the cell at [r][c]
    public void set(int r, int c, int value){
        grid[r][c].setValue(value);
    }
    //sets the value and if locked for the cell at [r][c]
    public void set(int r, int c, int value, boolean locked){
        grid[r][c].setValue(value);
        grid[r][c].setLocked(locked);
    }
    //It read the file and gives the cell value
    public boolean read(String filename) {
        try {
            FileReader file = new FileReader(filename);
            BufferedReader buffer = new BufferedReader(file);
            String line = buffer.readLine();
            int r = 0;
            while (line != null){
                String [] split = line.split("[ ]+");
                for ( int c = 0; c < split.length; c++){
                    int x = Integer.parseInt(split[c]);
                    grid[r][c].setValue(x);
                }
                r += 1;
                line = buffer.readLine();
            }
            buffer.close();
            return true;
        }
        catch(FileNotFoundException ex) {
            System.out.println("Board.read():: unable to open file " + filename );
        }
        catch(IOException ex) {
            System.out.println("Board.read():: error reading file " + filename);
        }

        return false;
    }
    //checks if the value is valid
    public boolean validValue(int row, int col, int value){
        //if the value is between 1 and 9
        if (value < 1 || value > 9){
            System.out.println("The value is out of bound");
            return false;
        }
        for (int i = 0; i < this.Size; i++){
            if (i != row){
                //on a row, should not be the same
                if (grid[i][col].getValue() == value){
                    return false;
                }
            }
            
            if (i != col){
                //on a column, should not be the same
                if (grid[row][i].getValue() == value){
                    return false;
                }
            }
        }
        int y = row/3;
        int x = col/3;
        for (int r = 0; r < this.Size; r++){
            for(int c = 0; c < this.Size; c++){
                if (r/3 == y && c/3 == x && r != row && c != col){
                    //in a 3x3 box, should not be the same
                    if (grid[r][c].getValue() == value){
                        return false;
                    }
                }
            }
        }
        return true;
    }
    //tells if the board is valid
    public boolean validSolution(){
        for (int r = 0; r < this.Size; r++){
            for (int c = 0; c < this.Size; c++){
                if (grid[r][c].getValue() == 0 || validValue(r, c, grid[r][c].getValue()) == false){
                    return false;
                } 
            }   
        }
        return true;
    }
    //This find the next cell that need to be given a value
    public Cell findBestCell(){
        int y = 0;
        for (int r = 0; r < this.Size; r++){
            for (int c = 0; c < this.Size; c++){
                //find the first cell with a 0 value
                if (grid[r][c].getValue() == 0){
                    for (int x = 1; x < 10; x++){
                        
                        if (validValue(r, c, x) == true){
                            grid[r][c].setValue(x);
                            return grid[r][c];
                        }
                    }
                    return null;
                }
            }
        }
        return null;
    }
    //This draw the whole board
    public void draw(Graphics g, int scale){
        for (int r = 0; r < this.Size; r++){
            for (int c = 0; c < this.Size; c++){
                grid[r][c].draw(g, c, r, scale);
                if (c == 2 || c == 5){
                    g.drawLine((int)((c + 1.5) * scale), (int)((0 - 0.5) * scale), (int)((c + 1.5) * scale), (this.Size + 1) * scale);
                }
            }
            if (r == 2 || r == 5){
                g.drawLine((0) * scale , (int)((r + 1.5) * scale), (this.Size + 1) * scale, (int)((r + 1.5) * scale));
        }
    }
    g.drawString("The Sudoku", (int)((this.Size/2) * scale), (int)(0.5 * scale));
    }
    public static void main(String [] args){
        Board b1 = new Board();
        b1.read(args[0]);
        System.out.println(b1);
        System.out.println(b1.validValue(1, 1, 4));
        System.out.println(b1.validValue(1, 8, 2));
        System.out.println(b1.validValue(8, 8, 5));
        System.out.println(b1.validValue(8, 8, 10));
        System.out.println(b1.validSolution());
    }
}