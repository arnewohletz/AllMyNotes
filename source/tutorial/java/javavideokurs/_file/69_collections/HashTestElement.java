package klassen;

public class HashTestElement {

	private int x;
	private int y;
	private int z;

	public HashTestElement(int x, int y, int z){
		this.x = x;
		this.y = y;
		this.z = z;
	}

	@Override
	public boolean equals(Object obj){
		if (!(obj instanceof HashTestElement)){
			return false;
		}
		HashTestElement e = (HashTestElement) obj;
		return e.x == this.x && e.y == this.y && e.z == this.z;
	}

	@Override
	public int hashCode(){
		return x*30 + y*12 + z*45;
	}

}