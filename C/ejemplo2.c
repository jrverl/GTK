#include <gtk/gtk.h>
 #include <webkit2/webkit2.h>
GtkWidget *cb1,*cb2,*cb3,*cb4;

static void
button_clicked (GtkButton *button,
                gpointer   user_data)
{
  GtkWindow *window = user_data;	
  
  if (gtk_toggle_button_get_active (GTK_TOGGLE_BUTTON(cb1))){
	 g_print ("Java\n");
	GtkWidget *webbrowser = Gtk_window_new (GTK_WINDOW_TOP_LEVEL);
	GtkWidget *scrolerview = Gtk_scroled_window_new (NULL,NULL);
	GtkWidget *webview = webkit_web_view_new();
	gtk_container_add(Gtk_container(scrolerview),webview);
	gtk_container_add(Gtk_container(webbrowser),scrollerview);
	
	webkit_web_view_load_uri(WEBKIT_WEB_VIEW(webview),"www.google.com");
	gtk_window_set_default__size(GTK_WINDOW(webbrowser),800,600);
	gtk_widget_show_all(webbrowser);
 }	
      	  	
}

int main(int argc, char *argv[])
{
	GtkWidget *window,*label,*b1,*b2,*grid;
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
	//b1 = gtk_link_button_new_with_label("google.com.pe")
	b2 = gtk_button_new_with_label ("Quit");


	gtk_container_add (GTK_CONTAINER (window), grid);

	gtk_grid_attach  (GTK_GRID(grid),cb1,1,1,1,1);
	gtk_grid_attach  (GTK_GRID(grid),cb2,1,2,1,1);
	gtk_grid_attach  (GTK_GRID(grid),cb3,2,1,1,1);
	gtk_grid_attach  (GTK_GRID(grid),cb4,2,2,1,1);
	gtk_grid_attach  (GTK_GRID(grid),b1,1,3,1,1);
	gtk_grid_attach  (GTK_GRID(grid),b2,2,3,1,1);

	gtk_toggle_button_set_active (GTK_TOGGLE_BUTTON (cb1), FALSE);
	g_signal_connect (GTK_BUTTON (b1), "clicked", G_CALLBACK (button_clicked), G_OBJECT (window));
	g_signal_connect (window, "destroy", G_CALLBACK (gtk_main_quit),NULL); //para poder cerrar la vent.
//	g_signal_connect (GTK_TOGGLE_BUTTON (cb1), "toggled", G_CALLBACK (toggled_cb), window);	
	
	gtk_widget_show_all (window);
	gtk_main();
	return 0;
}
