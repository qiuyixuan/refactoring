/**
*File: CellStack.java
*Author: Xiangxi Mu
*Date: 09/20/2020
 */
import java.util.Arrays;
public class CellStack{
    private Cell stack[];
    private int maxitem;
    //top is the next empty location
    private int top;
    //default constructor
    public CellStack(){
        this.maxitem = 15;
        this.top = 0;
        this.stack = new Cell [maxitem];
    }
    //constructor with max
    public CellStack(int max){
        this.maxitem = max;
        this.top = 0;
        this.stack = new Cell [maxitem];
    }
    //add new cell
    public void push(Cell c){
        //if there is no free location, double the capacity
        if (this.top == this.maxitem){
            this.maxitem = this.maxitem * 2;
            Cell [] newStack = new Cell [this.maxitem];
            for (int i = 0; i < this.top; i++){
                newStack[i] = stack[i];
            } 
            this.stack = newStack;
        }
        this.stack[this.top] = c;
        this.top += 1;
    }
    //remove the highest cell and return it
    public Cell pop(){
        Cell pop = new Cell();
        if (this.top == 0){
            System.out.println("The stack is empty");
            return pop;
        }
        this.top -= 1;
        pop = this.stack[this.top];
        return pop;
    }
    //return the size of the stack
    public int size(){
        return this.top;
    }
    public boolean empty(){
        return this.top == 0;
    }
}