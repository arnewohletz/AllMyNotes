package klassen.pcp;

public class Pipeline
{
	private Object data = null;

	//beide Methoden m�ssen synchronisiert sein, damit keine race conditions auftreten:
	//z.B. Thread 1 in der put-Methode stellt fest das data != null ist, springt zur Zuweisung. Daraufhin wird auf Thread 2 gewechselt.
	//dieser betritt ebenfalls die put-Methode, da data immer noch null ist macht er eine Zuweisung. Danach wird wieder auf Thread 1 gewechselt
	//dieser vollendet seine Zuweisung und �berschreibt den Wert von Thread 2 (lost update)

	//oder Thread 1 in der get-Methode stellt fest, dass data != null, springt zur Zuweisung. Daraufhin wird auf Thread 2 gewechselt.
	//dieser betritt  ebenfalls die put-Methode, da data immer noch ungleich null ist, wei�t das Objekt zu und l�scht es daraufhin. Danach wird wieder
	//auf Thread 1 gewechselt, dieser vollendet seine Zuweisung, setzt damit theData auf null (non repeatable read)

	//etwas hineinlegen sofern noch nichts drin ist
	public synchronized void put(Object newData)
	{
		System.out.println("Producer " + Thread.currentThread().getName() + " entered put()...");
		while (data != null)
		{
			try
			{
				this.wait();
			}
			catch (InterruptedException e)
			{
				e.printStackTrace();
			}
		}
		data = newData;
		System.out.println("Producer " + Thread.currentThread().getName() + " put data: " + data);
		this.notifyAll();
	}

	//etwas herausholen sofern etwas drin ist
	public synchronized Object get()
	{
		System.out.println("Consumer entered get()...");
		while (data == null)
		{

			try
			{
				this.wait();
			}
			catch (InterruptedException e)
			{
				e.printStackTrace();
			}

		}
		Object theData = data;
		data = null;
		System.out.println("Consumer retrieved data: " + theData);
		this.notifyAll();
		return theData;
	}
}
