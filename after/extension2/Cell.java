/**
*File: Cell.java
*Author: Xiangxi Mu
*Date: 09/20/2020
 */
import java.awt.Graphics;
import java.util.Arrays;
import java.awt.Color;
public class Cell{
    private int row;
    private int col;
    private int value;
    private boolean locked;
    //This is the default constructor
    public Cell(){
        this.row = 0;
        this.col = 0;
        this.value = 0;
        this.locked = false;
    }
    //Constructor with locked being false
    public Cell(int row, int col, int value){
        this.row = row;
        this.col = col;
        this.value = value;
        this.locked = false;
    }
    //Constructor with the locked determined by user
    public Cell(int row, int col, int value, boolean locked){
        this.row = row;
        this.col = col;
        this.value = value;
        this.locked = locked;
    }
    //Return the row
    public int getRow(){
        return this.row;
    }
    //Return the column
    public int getCol(){
        return this.col;
    }
    //Return the value
    public int getValue(){
        return this.value;
    }
    //Change the value
    public void setValue(int newval){
        this.value = newval;
    }
    //Return the locked
    public boolean isLocked(){
        return this.locked;
    }
    //Change the locked
    public void setLocked(boolean lock){
        this.locked = lock;
    }
    //Make a copy of the cell
    public Cell clone(){
        Cell newCell = new Cell(this.row, this.col, this.value, this.locked);
        return newCell;
    }
    //return the value as a string
    public String toString(){
        String result = Integer.toString(this.value);

        return result;
    }
    //draws the cell
    public void draw(Graphics g, int x0, int y0, int scale){
        char array[] = new char[] {(char)('0' + this.value), 0};
        if ( this.value == 0){
            g.setColor(Color.black);
            g.drawChars(array, 0, 1, (x0 + 1) * scale, (y0 + 1) * scale);
        }
        if ( this.value == 1){
            g.setColor(Color.red);
            g.drawChars(array, 0, 1, (x0 + 1) * scale, (y0 + 1) * scale);
        }
        if ( this.value == 2){
            g.setColor(Color.blue);
            g.drawChars(array, 0, 1, (x0 + 1) * scale, (y0 + 1) * scale); 
        }
        if ( this.value == 3){
            g.setColor(Color.green);
            g.drawChars(array, 0, 1, (x0 + 1) * scale, (y0 + 1) * scale); 
        }
        if ( this.value == 4){
            g.setColor(Color.pink);
            g.drawChars(array, 0, 1, (x0 + 1) * scale, (y0 + 1) * scale); 
        }
        if ( this.value == 5){
            g.setColor(Color.yellow);
            g.drawChars(array, 0, 1, (x0 + 1) * scale, (y0 + 1) * scale); 
        }
        if ( this.value == 6){
            g.setColor(Color.gray);
            g.drawChars(array, 0, 1, (x0 + 1) * scale, (y0 + 1) * scale); 
        }
        if ( this.value == 7){
            g.setColor(Color.magenta);
            g.drawChars(array, 0, 1, (x0 + 1) * scale, (y0 + 1) * scale); 
        }
        if ( this.value == 8){
            g.setColor(Color.cyan);
            g.drawChars(array, 0, 1, (x0 + 1) * scale, (y0 + 1) * scale); 
        }
        if ( this.value == 9){
            g.setColor(Color.orange);
            g.drawChars(array, 0, 1, (x0 + 1) * scale, (y0 + 1) * scale); 
        }                
    }
    public static void main(String [] args){
        Cell myCell = new Cell();
        Cell yourCell = new Cell(2, 2, 3);
        Cell hisCell = new Cell(2, 2, 3, true);
        System.out.println(myCell.getRow());
        System.out.println(myCell.getCol());
        System.out.println(myCell.getValue());
        System.out.println(myCell.isLocked());
        System.out.println(yourCell.getRow());
        System.out.println(yourCell.getCol());
        System.out.println(yourCell.getValue());
        System.out.println(yourCell.isLocked());
        System.out.println(hisCell.getRow());
        System.out.println(hisCell.getCol());
        System.out.println(hisCell.getValue());
        System.out.println(hisCell.isLocked());
        hisCell.setLocked(false);
        System.out.println(hisCell.toString());

    }
}