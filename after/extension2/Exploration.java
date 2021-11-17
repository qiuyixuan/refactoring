/**
*File: Exploration.java
*Author: Xiangxi Mu
*Date: 09/21/2020
 */
public class Exploration{
    public static void main(String [] args){
        if (args.length < 2){
            System.out.println("Usage: requires two command line arguments" +
            " \n The first is for number of initial values" +
            " \n The second is for number of simulations");
        }
        int count = 0;
        //numbers of initial values
		int initialVal = Integer.parseInt(args[0]);
        //The times to run the simulation
        int times = Integer.parseInt(args[1]);
		for(int i = 0; i < times; i++) {
			Sudoku simulation = new Sudoku(initialVal);
			boolean solved =simulation.solve(0);
			if(solved) {
				count++;
			}
			
		}
		System.out.println("The simulation with " + initialVal + " initial values are solved " + count + " times when there are total " + times + " simulations");
    }
}