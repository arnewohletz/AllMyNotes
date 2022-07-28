package programme;

import klassen.MyTask;

public class MultiThreadingDemo
{

	public static void main(String[] args)
	{
//		int threads = 4;
//
//		for(int i = 1; i <= threads; i++){
//			MyTask t = new MyTask();
//			Thread thread = new Thread(t);
//			thread.start();
//		}

		MyTask t = new MyTask();
		new Thread(t).start();

		System.out.println("MAIN-THREAD L�UFT...");
		try
		{
			Thread.sleep(3000);
		}
		catch (Exception e)
		{
			e.printStackTrace();
		}

		synchronized(t){
			t.cancel();
		}


	}

}
