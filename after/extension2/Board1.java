/**
*File: Board.java
*Author: Xiangxi Mu
*Date: 09/20/2020
 */
import java.awt.Graphics;
import java.io.*;
import java.util.Arrays;
import java.util.ArrayList;
public class Board1{
    private Cell [][] grid;
    public static final int Size = 9;
    //default constructor
    public Board1(){
        grid = new Cell [Board1.Size][Board1.Size];
        for ( int r = 0; r < Board1.Size; r++){
            for ( int c = 0; c < Board1.Size; c++){
                grid[r][c] = new Cell(r, c, 0);
            }
        }
    }
    public String toString(){
        String result = "";
        for ( int r = 0; r < Board1.Size; r++){
            for (int c = 0; c < Board1.Size; c++){
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
    public static void main(String [] args){
        Board1 b1 = new Board1();
        b1.read(args[0]);
        System.out.println(b1);
    }
}