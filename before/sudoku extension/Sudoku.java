/**
*File: Sudoku.java
*Author: Xiangxi Mu
*Date: 09/21/2020
 */
import java.util.Random;
import java.util.Arrays;
public class Sudoku{
    private Board board;
    private LandscapeDisplay display;
    //This is the default constructor with every value = 0
    public Sudoku(){
        board = new Board();
        display = new LandscapeDisplay(board, 30);
    }
    //This is the constructor that takes the number of locked numbers
    public Sudoku(int N){
        board = new Board();
        Random ran = new Random();
        int validNum = 0;
        while (validNum < N) {
            int row = ran.nextInt(board.getRows());
            int col = ran.nextInt(board.getCols());
            int val = ran.nextInt(board.Size) + 1;
            if (board.value(row, col) == 0 && board.validValue(row, col, val) == true){
                board.set(row, col, val, true);
                validNum += 1;
            }
        }
        display = new LandscapeDisplay(board, 50);
    }
    //This is the function that solve the sudoku
    public boolean solve(int delay){
        int time = 0;
        CellStack stack = new CellStack();
        int locked = board.numLocked();
        System.out.println("locked" + locked);
        while (stack.size() < board.Size * board.Size - locked){
            time++;
            //This draws the graph
            if( delay > 0 ) {
                try {
                    Thread.sleep(delay);
                }
                catch(InterruptedException ex) {
                    System.out.println("Interrupted");
                }
                display.repaint();
            }
            Cell nextCell = board.findBestCell();
            if (nextCell != null){
                stack.push(nextCell);
                //System.out.println(stack.size());
                board.set(nextCell.getRow(), nextCell.getCol(), nextCell.getValue());
            }
            else{
                    boolean stuck = true;
                    while (stuck && stack.size() > 0){
                        Cell pop = stack.pop();
                        for ( int n = pop.getValue() + 1; n < 10; n++){
                            if (board.validValue(pop.getRow(), pop.getCol(), n) == true){
                                pop.setValue(n);
                                stack.push(pop);
                                board.set(pop.getRow(), pop.getCol(), n);
    
                                stuck = false;
                                break;
                            }
                        }
                        if (stuck){

                        board.set(pop.getRow(), pop.getCol(), 0);
                        }
                    }
                
                if (stack.size() == 0){
                    System.out.println("time is:" + time);
                    System.out.println(stack.size());

                    return false;

                }
            }
        }
        System.out.println("time is:" + time);
        display.repaint();

        //System.out.println(stack.size());
        return true;
    }
    public static void main(String [] args){
        int N = Integer.parseInt(args[0]);
        int delay = Integer.parseInt(args[1]);
        //String fileName = args[2];
        Sudoku s1 = new Sudoku(N);
        //System.out.println(s1.board);
        //s1.solve(Integer.parseInt(args[1]));
        //System.out.println(s1.board);
        //s1.board.read(fileName);
        System.out.println(s1.board);
        //System.out.println(s1.board.numLocked());
        System.out.println(s1.solve(delay));
        System.out.println(s1.board);

    }
}