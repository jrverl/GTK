#include <gtk/gtk.h>
int main(int argc, char *argv[])
{
	GtkWidget *window,*label,*b1,*b2,*grid,*cb1,*cb2,*cb3,*cb4;
	gtk_init (&argc, &argv);

	window = gtk_window_new (GTK_WINDOW_TOPLEVEL);
	gtk_window_set_default_size (GTK_WINDOW(window),200,100);
	gtk_window_set_title (GTK_WINDOW (window), "Languge Selector");

	label =  gtk_label_new ("Select Language");
	grid = gtk_grid_new();

	cb1 = gtk_check_button_new_with_label("Java");
	cb2 = gtk_check_button_new_with_label("Python");
	cb3 = gtk_check_button_new_with_label("C");
	cb4 = gtk_check_button_new_with_label("JavaScript");

	b1 = gtk_button_new_with_label ("Learn");
	b2 = gtk_button_new_with_label ("Quit");


	gtk_container_add (GTK_CONTAINER (window), grid);

	gtk_grid_attach  (GTK_GRID(grid),cb1,1,1,1,1);
	gtk_grid_attach  (GTK_GRID(grid),cb2,1,2,1,1);
	gtk_grid_attach  (GTK_GRID(grid),cb3,2,1,1,1);
	gtk_grid_attach  (GTK_GRID(grid),cb4,2,2,1,1);
	gtk_grid_attach  (GTK_GRID(grid),b1,1,3,1,1);
	gtk_grid_attach  (GTK_GRID(grid),b2,2,3,1,1);


	g_signal_connect (window, "destroy", G_CALLBACK (gtk_main_quit),NULL);
	
	gtk_widget_show_all (window);
	gtk_main();
	return 0;
}
