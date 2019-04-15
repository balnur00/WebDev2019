import { Injectable } from '@angular/core';
import {MainService} from './main.service';
import { TaskList, Task } from '../models/model';
import { HttpClient } from '@angular/common/http';

@Injectable({
  providedIn: 'root'
})
export class ProviderService extends MainService{

  constructor(http: HttpClient) {
    super(http);
  }

  getTasksList(): Promise<TaskList[]> {
    return this.get('http://localhost:8000/api/tasklist/', {});
  }
  getTasks(id: number): Promise<Task[]> {
    return this.get(`http://localhost:8000/api/tasklist/${id}/task`, {});
  }
  createTaskList(name: any): Promise<TaskList> {
    return this.post('http://localhost:8000/api/tasklist/', {
      name
    });
  }
  updateTaskList(tasklist: TaskList): Promise<TaskList> {
    return this.put(`http://localhost:8000/api/tasklist/${tasklist.id}/`, {
      name : tasklist.name
    });
  }
  deleteTaskList(tasklist: TaskList): Promise<TaskList> {
    return this.delet(`http://localhost:8000/api/tasklist/${tasklist.id}/`, {});
  }
  createTask(tasklist: TaskList, name: any, createdAt: any, dueOn: any, status: any): Promise<Task> {
    return this.post(`http://localhost:8000/api/tasklist/${tasklist.id}/task`, {
      name,
      createdAt,
      dueOn,
      status
    });
  }
}
