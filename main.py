"""
the application detection eartquake
Modularisation with function
Modularisation with package
"""
import recentearthquake

if __name__ == '__main__':
    print('The main appication')
    result = recentearthquake.extration_data()
    recentearthquake.show_data(result)
