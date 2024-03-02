package klassen.pcp;

public class Producer implements Runnable
{

	private final Pipeline pipeline;

	public Producer(Pipeline pipeline)
	{
		this.pipeline = pipeline;
	}

	@Override
	public void run()
	{
		int dataCount = 0;

		for (int i = 0; i < 100; i++)  //Es wird 100 x Mal etwas in die Pipeline gelegt
		{
			System.out.println("Producer " + Thread.currentThread().getName() + " wants to enter put()...");
			pipeline.put(new String("Data " + ++dataCount + " from " + Thread.currentThread().getName()));

			try
			{
				Thread.sleep((long) (Math.random() * 5000));
			}
			catch (InterruptedException e)
			{
				e.printStackTrace();
			}

		}
	}
}
