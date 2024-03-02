package programme;

import java.util.HashMap;
import java.util.HashSet;
import java.util.Map;
import java.util.Random;
import java.util.Set;

import klassen.HashTestElement;

public class HashPerformanceDemo {

	public static void main(String[] args) {

		HashTestElement[] elements = new HashTestElement[1000000];
		Random r = new Random();
		for (int i = 0; i < elements.length; i++) {
			int x = r.nextInt();
			int y = r.nextInt();
			int z = -(x + y);
			if (x + y + z != 0){
				throw new IllegalStateException();
			}
			elements[i] = new HashTestElement (x,y,z);
		}
		
		Set<HashTestElement>set = new HashSet<HashTestElement>();
		
		long start =  System.currentTimeMillis();
		for (HashTestElement e : elements){
			set.add(e);
		}
		for(HashTestElement e : elements){
			set.contains(e);
		}
		for(HashTestElement e : elements){
			set.remove(e);
		}
		long end = System.currentTimeMillis();
		System.out.println("Benötigte Zeit: " + (end - start) / 1000 + " Sekunden");
		
		Map<String, Integer> map = new HashMap<String, Integer>();
		map.put("BMW", 12);
		map.put("Audi", 8);
		int i = map.get("BMW");

	}

}