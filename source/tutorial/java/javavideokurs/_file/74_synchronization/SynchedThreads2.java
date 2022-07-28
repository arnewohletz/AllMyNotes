package programme;

public class SynchedThreads2 implements Runnable
{
	//static Object lock = new Object();

	int x;

	@Override
	public void run() {
		int i;
		for ( i = 0; i < 2000; i++){
			synchronized(this){
				x++;
			}
		}
		System.out.println(Thread.currentThread().getName() + " has finished after " + i + " loops");
	}

	public static void main(String[] args){

		SynchedThreads2 c = new SynchedThreads2();
		new Thread(c).start(); //Thread wird ohne Zuweisung an eine Variable gestartet
		new Thread(c).start(); //Thread wird abermals gestartet

		//Achtung: Beide Threads durchlaufen zeitgleich die run() Methode, d.h. erh�hen die Instanzvariable x
		//Die lokale Variable i teilen sich die beiden Threads nicht, sondern jeder besitzt ein eigenes lokales i

		try
		{
			Thread.sleep(5000);
		}
		catch (InterruptedException e)
		{
			e.printStackTrace();
		}

		synchronized(c){
			System.out.println("x is: " + c.x);
		}

		/*Ausgabe ist bei jeder Ausf�hrung unterschiedlich:
		Thread-1 has finished after 2000 loops
		Thread-0 has finished after 2000 loops
		x is: 3291
		- x ist h�ufig nicht die Summe aus Thread 1 und 2 (sollte stets 4000 sein)
		*/
	}

}
