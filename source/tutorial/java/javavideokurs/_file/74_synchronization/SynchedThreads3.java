package programme;

public class SynchedThreads3 implements Runnable
{

	int x;

	@Override
	public void run()
	{
		int loops = 0;

		//x wird erh�ht, bis 10000 erreicht ist (egal welcher Thread x wie oft erh�ht)
		while (true)
		{
			synchronized (this)
			{
				if (x < 10000)
				{
					x++;
					loops++;
				}
				else
				{
					break;
				}
			}
		}
		System.out.println(Thread.currentThread().getName() + " has finished after " + loops + " loops");
	}

	public static void main(String[] args)
	{
		SynchedThreads3 a = new SynchedThreads3();
		new Thread(a).start();
		new Thread(a).start();

		try
		{
			Thread.sleep(500);
		}
		catch (InterruptedException e)
		{
			e.printStackTrace();
		}
		synchronized (a)
		{
			System.out.println("x is: " + a.x);
		}

		/*
		 * Ausgabe ist bei jeder Ausf�hrung unterschiedlich, da man nicht
		 * beeinflussen kann, welcher Thread wann startet (Scheduling): Thread-1
		 * has finished after 6305 loops Thread-0 has finished after 8700 loops
		 * x is: 10001 - x(thread1) + x(thread2) ist stets �ber 10000 (sollte in
		 * der Summe genau 10000 sein) - x ist manchmal auch mehr als 10000
		 * (sollte auch stets 10000 sein)
		 */
	}

}
