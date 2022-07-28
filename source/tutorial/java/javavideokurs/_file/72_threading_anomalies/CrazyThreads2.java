package programme;

public class CrazyThreads2 implements Runnable
{
	int x;

	@Override
	public void run() {
		int i;
		for ( i = 0; i < 2000; i++){
			x++;
		}
		System.out.println(Thread.currentThread().getName() + " has finished after " + i + " loops");
	}

	public static void main(String[] args){

		CrazyThreads2 c = new CrazyThreads2();
		new Thread(c).start(); //Thread wird ohne Zuweisung an eine Variable gestartet
		new Thread(c).start(); //Thread wird abermals gestartet

		//Achtung: Beide Threads durchlaufen zeitgleich die run() Methode, d.h. erh�hen die Instanzvariable x
		//Die lokale Variable i teilen sich die beiden Threads nicht, sondern jeder besitzt ein eigenes lokales i

		try
		{
			Thread.sleep(500);
		}
		catch (InterruptedException e)
		{
			e.printStackTrace();
		}

		System.out.println("x is: " + c.x);
		/*Ausgabe ist bei jeder Ausf�hrung unterschiedlich:
		Thread-1 has finished after 2000 loops
		Thread-0 has finished after 2000 loops
		x is: 3291
		- x ist h�ufig nicht die Summe aus Thread 1 und 2 (sollte stets 4000 sein)
		*/
	}
}
