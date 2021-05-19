import java.util.*;

public class ����Ԫ���� {
	private static double mutate_rate = 0.001;
	private static double cover_P = 0.6;
	private static int group_size = 20;
	private static int DNA_size = 30;
	private static int count = 1000;

	private static double[] possible;

	public static void main(String[] args) {
		// TODO �Զ����ɵķ������
		ArrayList<Node> group = init_grop(group_size);
		for (int i = 0; i < 20; i++) {
			possible = cal_possible(group);
			group = cors_sover(group);
			mutate_child(group);
			Node best = find_best(group);
			System.out.println(String.format("----------��%d��----------", i + 1));
			System.out.println(String.format("���ֵΪ��%f xΪ��%f yΪ��%f", best.fitness, best.x, best.y));
		}
	}

	// ��ʼ����Ⱥ
	static ArrayList<Node> init_grop(int size) {
		ArrayList<Node> grop = new ArrayList<Node>();
		for (int i = 0; i < size; i++) {
			Node t;
			do {
				t = new Node();
			} while (t.fitness <= 0);
			grop.add(t);
		}
		return grop;
	}

	// ����ͻ��
	static void mutate_child(ArrayList<Node> father_group) {
		Random random = new Random();
		for (Node c : father_group) {
			if (random.nextDouble() < mutate_rate) {
				int k = random.nextInt(30);
				c.DNA[k] = (c.DNA[k] + 1) % 2;
				c.cal();
			}
		}
	}

	// ѡ�񸸸���
	static Node sel_father(ArrayList<Node> father_group) {
		Random random = new Random();
		double t = random.nextDouble();
		int i;
		for (i = 0; i < father_group.size() - 1; i++) {
			if (t < possible[i])
				return father_group.get(i);
		}
		return father_group.get(i);
	}

	// ��ֳ
	static Node get_child(ArrayList<Node> father_group) {
		Node parent1 = sel_father(father_group);
		Node parent2 = sel_father(father_group);
		int[] tmp = new int[DNA_size];
		Random random = new Random();
		int position = random.nextInt(DNA_size);
		for (int i = 0; i < position; i++) {
			tmp[i] = parent1.DNA[i];
		}
		for (int i = position; i < DNA_size; i++) {
			tmp[i] = parent2.DNA[i];
		}
		Node child = new Node(tmp);
		if (child.fitness < 0 || child.fitness < parent1.fitness || child.fitness < parent2.fitness)
			child = get_child(father_group);
		return child;
	}

	// ����
	static ArrayList<Node> cors_sover(ArrayList<Node> father_group) {
		ArrayList<Node> new_grop = new ArrayList<Node>();
		Random random = new Random();
		for (int k = 0; k < father_group.size(); k++) {
			new_grop.add(get_child(father_group));
		}
		return new_grop;
	}

	// ����ÿ���ڵ㱻��ȡ���ļ���
	static double[] cal_possible(ArrayList<Node> group) {
		double[] fitness = new double[group.size()];
		double total = 0;
		// ������ֵ���ۼ���Ӧ��
		for (int i = 0; i < group.size(); i++) {
			total += group.get(i).fitness;
			fitness[i] = total;
		}
		for (int i = 0; i < group.size(); i++) {
			fitness[i] /= total;
		}
		return fitness;
	}

	// ���ҵ�ǰ����ֵ
	static Node find_best(ArrayList<Node> group) {
		Node best = group.get(0);
		for (Node c : group) {
			if (c.fitness > best.fitness)
				best = c;
		}
		return best;
	}
}

class Node {
	int[] DNA = new int[30];
	double x;
	double y;
	double fitness;

	public Node() {
		for (int i = 0; i < 30; i++) {
			DNA[i] = new Random().nextBoolean() ? 1 : 0;
		}
		cal();
	}

	public Node(int[] DNA) {
		for (int i = 0; i < DNA.length; i++) {
			this.DNA[i] = DNA[i];
		}
		cal();
	}

	// ����ת��
	double Translate(int index) {
		double ans = 0;
		for (int i = index; i < index + 15; i++) {
			ans = ans * 2 + DNA[i];
		}
		return (ans - 16384) / 16384;
	}

	// ��Ӧ�ȼ���
	double cal_Fitness() {
		return x * Math.sin(4 * Math.PI * x) - y * Math.sin(4 * Math.PI * y + Math.PI) + 1;
	}

	// ����
	void cal() {
		x = Translate(0);
		y = Translate(15);
		fitness = cal_Fitness();
	}
}